from django.db import models


# Create your models here.
"""create author model"""
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
"""create book model with a foreign key to Author model
it has a many to one relationship (foreignkey) to the Author model, 
(many books can have one author)"""

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title