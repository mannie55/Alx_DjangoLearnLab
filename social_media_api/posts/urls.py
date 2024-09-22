from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostFeedViewSet
from .views import LikePostView, UnlikePostView, CommentOnPostView


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)



urlpatterns = [
    path('<int:pk>/comment/', CommentOnPostView.as_view(), name='comment_on_post'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
    path('feed/', PostFeedViewSet.as_view(), name='post_feed'),
    path('', include(router.urls)),
]