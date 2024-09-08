from rest_framework import serializers
from .models import Author, Book
import datetime





"""author serializer that serializes the author class.
The relationship between author and book is handled using nested serializers
"""


from rest_framework import serializers
from .models import Author, Book
import datetime

"""The BookSerializer serializes all fields of the Book model, 
including the author field, which holds a reference to an Author"""
class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name', read_only=True)  # Show author name, not the entire nested object

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('The publication year cannot be in the future.')
        return value

"""author serializer that serializes the author class.
The relationship between author and book is handled using nested serializers
"""
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True, source='book_set')

    class Meta:
        model = Author
        fields = ['name', 'books']
