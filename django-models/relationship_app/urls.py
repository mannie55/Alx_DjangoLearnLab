from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register, Login, Logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]