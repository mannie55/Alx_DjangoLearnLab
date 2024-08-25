from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from .models import Book
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        book = Book(title=title, author_id=author_id)  
        book.save()
        return redirect('book_list') 
    else:
        return render(request, 'relationship_app/add_book.html', raise_exception=True)


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('book_detail', pk=book.pk)
    else:
        context = {'book': book}
        return render(request, 'relationship_app/edit_book.html', context)


@permission_required('bookshelf.can_delete')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
    return redirect('book_list') 
