from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin
from .models import CustomUser



admin.site.register(CustomUser, CustomUserAdmin)

# customise Book 
class Book_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filters = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

# Register your models here.
admin.site.register(Book, Book_admin)