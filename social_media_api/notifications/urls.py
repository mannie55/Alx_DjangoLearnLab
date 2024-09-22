# notifications/urls.py
from django.urls import path
from .views import get_notifications, mark_as_read

urlpatterns = [
    path('', get_notifications, name='get_notifications'),
    path('mark-as-read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
]

