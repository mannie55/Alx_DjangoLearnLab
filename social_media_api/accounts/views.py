from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from notifications.models import Notification



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def get_queryset(self):
        return get_user_model().objects.all()

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        # Return a different status code based on whether the token is new or not
        response_status = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        }, status=response_status)
    
class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    



User = get_user_model()

class FollowViewSet(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        '''use get_object_or_404 insteand of User.objects.get for better error handling'''
        user_to_follow = get_object_or_404(User, id=self.kwargs['user_id'])

        if not user.following.filter(id=user_to_follow.id).exists():
            user.following.add(user_to_follow)  # Add to following
            '''create notification'''
            if user_to_follow != user:
                Notification.objects.create(
                    recipient=user_to_follow,
                    actor=user,
                    verb='started following you'
                )
                return redirect('profile', user_id=user_to_follow.id)
            return Response({"detail": "User followed successfully"}, status=status.HTTP_200_OK)
        
        return Response({"detail": "User already followed"}, status=status.HTTP_400_BAD_REQUEST)
    

class UnfollowViewSet(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user  # The current logged-in user (the one who is trying to unfollow)
        user_to_unfollow = get_object_or_404(User, pk=self.kwargs['user_id'])  # The user to be unfollowed

        # Check if the user is following the user_to_unfollow
        if user.following.filter(pk=user_to_unfollow.pk).exists():
            user.following.remove(user_to_unfollow)  # Unfollow the user
            return Response({"message": "User unfollowed successfully"}, status=200)

        return Response({"error": "You are not following this user"}, status=400)
    


