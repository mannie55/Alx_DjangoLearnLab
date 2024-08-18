from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]