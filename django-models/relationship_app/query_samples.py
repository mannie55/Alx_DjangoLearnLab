import os
import django

#setup django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.LibraryProject.settings")
django.setup()

#import models
from relationship_app.models import *

def query_book_by_authors(authorname):
    try:
        author = Author.objects.get(**authorname)   
        books = Book.objects.filter(author=author)
        for book in books:
            print(f"title: {book.title}, author: {author.name}")
    except Author.DoesNotExist:
        print("Author does not exist")