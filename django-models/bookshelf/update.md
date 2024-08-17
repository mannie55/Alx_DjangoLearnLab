<!-- retrieve -->
book = Book.objects.get(title="1984")
<!-- update -->
book.title = "Nineteen Eighty-Four"
<!-- save -->
book.save