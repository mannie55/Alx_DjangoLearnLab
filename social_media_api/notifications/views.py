# notifications/views.py
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.shortcuts import get_object_or_404

@login_required
def get_notifications(request):
    # Get unread notifications for the logged-in user
    notifications = Notification.objects.filter(recipient=request.user, is_read=False)
    
    data = [{
        "actor": notification.actor.username,
        "verb": notification.verb,
        "target": str(notification.target),
        "timestamp": notification.timestamp,
        "is_read": notification.is_read
    } for notification in notifications]

    return JsonResponse({"notifications": data}, status=200)

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.is_read = True
    notification.save()

    return JsonResponse({"message": "Notification marked as read"}, status=200)

