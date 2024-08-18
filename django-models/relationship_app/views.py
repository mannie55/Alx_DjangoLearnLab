from django.shortcuts import render, redirect
from .models import Library 
from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required


def user_is_admin(user):
    return user.userprofile.role == 'admin'

def user_is_librarian(user):
    return user.userprofile.role == 'librarian'

def user_is_member(user):
    return user.userprofile.role == 'member'

@user_passes_test(user_is_admin)
def admin_view(request):
    context = {'message': 'Welcome to the Admin Dashboard'}
    return render(request, 'relationship_app/admin_view.html', context)

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})