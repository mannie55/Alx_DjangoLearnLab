from django.urls import path
from .views import ListView, CreateView, DeleteView, DetailView, UpdateView,CreateListAuthorView
from rest_framework.authtoken import views

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('book/', ListView.as_view(), name='book_list'),
    path('book/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('book/', CreateView.as_view(), name='book-create'),
    path('author/', CreateListAuthorView.as_view(), name='author-create'),
    path('book/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]