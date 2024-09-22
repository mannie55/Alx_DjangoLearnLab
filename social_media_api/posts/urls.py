from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostFeedViewSet
from .views import like_post, unlike_post, comment_on_post


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)



urlpatterns = [
    path('<int:post_id>/comment/', comment_on_post, name='comment_on_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('unlike/<int:post_id>/', unlike_post, name='unlike_post'),
    path('feed/', PostFeedViewSet.as_view(), name='post-feed'),
    path('', include(router.urls)),
]