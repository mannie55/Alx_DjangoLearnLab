from django.shortcuts import render
from rest_framework import generics, mixins
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CreateListAuthorView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# Create your views here.
class ListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get_queryset(self):
    #     user = self.request.user
    #     return Book.objects.filter(author=user)


class DetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
# get all books
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class CreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
# Retrieves all books validates before creating
    def post(self, request, *args, **kwargs):
        publication_year = request.data.get('publication_year')
        if publication_year and int(publication_year) > datetime.now().year:
            return Response(
                {"error": "The publication year cannot be in the future."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.create(request, *args, **kwargs)



class UpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
# update book
    def put(self, request, *args, **kwargs):
        publication_year = request.data.get('publication_year')
        if publication_year and int(publication_year) > datetime.now().year:
            return Response(
                {"error": "The publication year cannot be in the future."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.update(request, *args, **kwargs)


class DeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
# deletes book, book is retrieved by including the primary key in the url
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
