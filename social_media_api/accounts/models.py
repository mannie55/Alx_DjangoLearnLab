from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_photo/', height_field=None, blank=True, null=True, max_length=100)
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_followers', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)
    

    def __str__(self):
        return self.username
