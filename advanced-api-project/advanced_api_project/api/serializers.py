from rest_framework import serializers
from .models import Author, Book
import datetime

"""The BookSerializer serializes all fields of the Book model, 
including the author field, which holds a reference to an Author"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'publication_year']

    def validate_publication_year(self, data):
        current_year = datetime.datetime.now().year
        if data > current_year:
            raise serializers.ValidationError('The publication year cannot be in the future.')
        return data
    




"""author serializer that serializes the author class.
The relationship between author and book is handled using nested serializers
"""


class AuthorSerializer(serializers.ModelSerializer):
    author_name = serializers.Charfield(source='Author.name', read_only=True)

    """The books field is a nested serializer,
    which dynamically serializes the related
    Book instances for each Author"""

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']