from django.urls import path
from .views import ListView, CreateView, DeleteView, DetailView, UpdateView,CreateListAuthorView
from rest_framework.authtoken import views

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('book-list/', ListView.as_view(), name='book_list'),
    path('book-detail/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('book-create/', CreateView.as_view(), name='book-create'),
    path('author-create-list/', CreateListAuthorView.as_view(), name='author-create'),
    path('book-update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]