# accounts/urls.py
from django.urls import path
from .views import UserRegistrationView, CustomAuthToken, UserProfileView
from .views import FollowViewSet, UnfollowViewSet
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('follow/<int:user_id>/', FollowViewSet.as_view, name='follow'),
    path('unfollow/<int:user_id>/', UnfollowViewSet.as_view(), name='unfollow'),
]
