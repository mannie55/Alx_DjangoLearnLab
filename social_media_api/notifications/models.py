from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_recieve')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_sent')
    verb = models.CharField(max_length=255)

    '''fields for geneicforeignkey to represent the target object'''
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')

    timestamp = models.DateTimeField(auto_now_add=True)
    '''to mark if the notification has been read'''
    is_read = models.BooleanField(default=False) 

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
       return f"{self.actor} {self.verb} {self.target} for {self.recipient}"