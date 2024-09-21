from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, PostFeedView


router = DefaultRouter()
router.register(r'posts/', PostViewSet)
router.register(r'comments/', CommentViewSet)
router.register(r'feed/', PostFeedView)


urlpatterns = [
    path('', include(router.urls)),
]