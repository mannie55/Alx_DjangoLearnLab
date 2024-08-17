<!-- import the model class book -->
 from bookshelf.models import Book

 <!-- create instance of Book and save-->
  book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
  book.save()