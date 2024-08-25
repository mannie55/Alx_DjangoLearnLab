from django.contrib import admin
from .models import Book

# customise Book 
class Book_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filters = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

# Register your models here.
admin.site.register(Book, Book_admin)