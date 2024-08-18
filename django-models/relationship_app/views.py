from django.shortcuts import render, redirect
from .models import Library, Book, UserProfile
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required


# Create your views here.
# Function to check if user is an Admin
def user_is_admin(user):
    return user.userprofile.role == 'admin'


# Function to check if user is a Librarian
def user_is_librarian(user):
    return user.userprofile.role == 'librarian'

# Function to check if user is a Member
def user_is_member(user):
    return user.userprofile.role == 'member'

# Admin View
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')



# Librarian View
@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# Member View
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