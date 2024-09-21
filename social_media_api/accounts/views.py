from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return get_user_model().objects.all()

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
         # Use the serializer to validate and save the new user
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # Create a token for the new user
        token, created = Token.objects.get_or_create(user=user)
         # Return the token and user details
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        }, status=status.HTTP_201_CREATED)
    
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


User = get_user_model()

class FollowViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        '''use get_object_or_404 insteand of User.objects.get for better error handling'''
        user_to_follow = get_object_or_404(User, id=self.kwargs['user_id'])

        if not user.following.filter(id=user_to_follow.id).exists():
            user.following.add(user_to_follow)  # Add to following
            return Response({"detail": "User followed successfully"}, status=status.HTTP_200_OK)
        
        return Response({"detail": "User already followed"}, status=status.HTTP_400_BAD_REQUEST)
    

class UnfollowViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user  # The current logged-in user (the one who is trying to unfollow)
        user_to_unfollow = get_object_or_404(User, pk=self.kwargs['user_id'])  # The user to be unfollowed

        # Check if the user is following the user_to_unfollow
        if user.following.filter(pk=user_to_unfollow.pk).exists():
            user.following.remove(user_to_unfollow)  # Unfollow the user
            return Response({"message": "User unfollowed successfully"}, status=200)

        return Response({"error": "You are not following this user"}, status=400)