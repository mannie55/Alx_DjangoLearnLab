from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from notifications.models import Notification



class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a post/comment to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        # So we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of the post/comment.
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        '''this sets the author to the current user before creating the post'''
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


    def perform_create(self, serializer):
        # Set the author to the current user before saving the comment.
        serializer.save(author=self.request.user)

class PostFeedViewSet(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        '''get the current logged in user'''
        user = request.user

        '''get all the users the current user is following'''
        following_users = user.following.all()

        '''get posts from the users that the current user follows'''
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
    





class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk, *args, **kwargs):
        # Retrieve the post by its primary key (pk)
        post = generics.get_object_or_404(Post, pk=pk)
        # Get or create the Like object for the current user and the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create notification for the post author if they are not the one liking the post
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb='liked your post',
                    target=post
                )
            return Response({"detail": "Post liked successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk, *args, **kwargs):
        # Retrieve the post by its primary key (pk)
        post = generics.get_object_or_404(Post, pk=pk)
        # Try to get the Like object
        like = Like.objects.filter(user=request.user, post=post).first()
        
        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "You haven't liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)



class CommentOnPostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the post object based on the primary key (pk)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        user = request.user

        # Get the comment text from the request data
        comment_text = request.data.get('comment')
        if not comment_text:
            return Response({"detail": "Comment content cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the comment
        comment = Comment.objects.create(post=post, author=user, content=comment_text)

        # Notify the post author about the new comment (if the commenter is not the author)
        if user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='commented on your post',
                target=post
            )

        # Return a success message
        return Response({"message": "Comment added successfully"}, status=status.HTTP_201_CREATED)