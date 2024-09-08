from django.urls import path
from .views import ListView, CreateView, DeleteView, DetailView, UpdateView,CreateListAuthorView
from rest_framework.authtoken import views

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('books/', ListView.as_view(), name='book_list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/create', CreateView.as_view(), name='book-create'),
    path('authors/', CreateListAuthorView.as_view(), name='author-create'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]