# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Replace with the fields you need
        # Optionally, you can add custom widgets or validation here

# If you need a general form and not related to a model, use:
class Example(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
