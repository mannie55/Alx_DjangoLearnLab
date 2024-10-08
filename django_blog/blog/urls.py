from django.urls import path
from .views import register, login_view, logout_view, home_view, profile_view
from .views import  PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView
from .views import CommentDeleteView, CommentUpdateView, CommentCreateView
from .views import search, PostByTagListView



urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('',home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('search/', search, name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'), 
]