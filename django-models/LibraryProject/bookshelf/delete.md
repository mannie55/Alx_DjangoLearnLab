<!-- import model -->
from bookshelf.models import Book
<!-- retrieve bookto delete -->
book = Book.objects.get(title="Nineteen Eighty-Four")
<!-- delete book -->
book.delete()
<!-- try to retrieve deleted book -->
book = Book.objects.get(title="Nineteen Eighty-Four")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\O AND A\.virtualenvs\0x1.Introduction__to__Django-nTZn9Wdl\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\O AND A\.virtualenvs\0x1.Introduction__to__Django-nTZn9Wdl\Lib\site-packages\django\db\models\query.py", line 649, in get
    raise self.model.DoesNotExist(
bookshelf.models.Book.DoesNotExist: Book matching query does not exist. 