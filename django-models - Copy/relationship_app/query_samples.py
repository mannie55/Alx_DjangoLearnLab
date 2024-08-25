import os
import django

#setup django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.LibraryProject.settings")
django.setup()

#import models
from relationship_app.models import *

def query_book_by_authors(author_name):
   
    try:
        author = Author.objects.get(name=author_name)   
        books = Book.objects.filter(author=author)
        for book in books:
            print(f"title: {book.title}, author: {author.name}")
    
    except Author.DoesNotExist:
        print("Author does not exist")

def books_in_library(library_name):

    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"title: {book.title}, library: {library.name}")
    
    except Library.DoesNotExist:
        print("Library does not exist")

def librarian_for_a_library(librarian_name):

    try:
        library = Librarian.objects.get(library="")
        librarian = library.librarian
        print(f"librarian: {librarian.name}, library: {library.name}")
    
    except Library.DoesNotExist:
        print("Library does not exist")