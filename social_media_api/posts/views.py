from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404, redirect
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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]
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
    




@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if not Like.objects.filter(post=post, user=user).exists():
        Like.objects.create(post=post, user=user)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target=post
        )
    return JsonResponse({"message": "Post liked successfully"}, status=200)


@login_required
def unlike_post(request, post_id):
    permission_classes = [IsAuthenticated]
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    # Check if the user has liked the post
    like = Like.objects.filter(post=post, user=user).first()
    if like:
        like.delete()
        return JsonResponse({"message": "Post unliked successfully"}, status=200)

    return JsonResponse({"message": "You have not liked this post"}, status=400)

@login_required
def comment_on_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    comment_text = request.POST.get('comment')

    # Create the comment
    comment = Comment.objects.create(post=post, author=user, content=comment_text)

    # Notify post author of the comment
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='commented on your post',
        target=post
    )

    return JsonResponse({"message": "Comment added successfully"}, status=200)