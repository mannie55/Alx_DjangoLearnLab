from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.contrib.auth import get_user_model



# # Create your models here.

# class CustomUserManager(BaseUserManager):
    
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('User must have email')
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         user = self.create_user(email, password, **extra_fields)

#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)

#         return user
        


# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_photo = models.ImageField(upload_to='profile_photos/', height_field=None, max_length=100)



#     objects = CustomUserManager()





class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

    


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book')
        ]

    def __str__(self):  
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name