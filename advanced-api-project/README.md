# Book & Author API

This project is a Django-based REST API to manage books and authors. The API provides endpoints for creating, retrieving, updating, and deleting books, as well as retrieving authors and their related books.

## Features:
- **Token Authentication**: Users must authenticate using a token for any actions requiring modification (POST, PUT, DELETE).
- **Permissions**:
  - Unauthenticated users can read data.
  - Authenticated users can create, update, and delete books.
  - Admins have full access.

## Models:
1. **Author**: 
    - Fields: `name`
    - Relationships: One-to-many with the `Book` model.
2. **Book**: 
    - Fields: `title`, `author` (ForeignKey), `publication_year`
    - Validation: The publication year must not be in the future.

## Serializers:
- **AuthorSerializer**: 
    - Nested serialization of books associated with the author.
- **BookSerializer**: 
    - Handles custom validation for publication year.

## Views:
- **CreateListAuthorView**: Create or list all authors
- **ListView**: Retrieves all books.
- **CreateView**: Allows authenticated users to create new books with validation.
- **DetailView**: Retrieves a single book by its ID.
- **UpdateView**: Allows updating a book (authenticated users).
- **DeleteView**: Allows deletion of a book (authenticated users).

## Permissions:
- `IsAuthenticatedOrReadOnly`: Allows unauthenticated users to read data, while authenticated users can modify it.
- `IsAdminUser`: Allows only admins to modify data.

## Token Authentication:
1. Obtain a token by sending a POST request with username and password to `/api/token/`.
2. Include the token in the `Authorization` header of any request requiring authentication.
   - Example:
     ```
     Authorization: Token your_token_here
     ```

## Endpoints:
- **POST** `api/author-create-list/`: Create a new author.
- **GET** `api/author-create-list/`: Retrieve all authors.
- **GET** `api/books-list/`: Retrieve all books.
- **POST** `api/books-create/`: Create a new book (authenticated).
- **GET** `api/books-retrieve/<id>/`: Retrieve a specific book.
- **PUT** `api/books-update/<id>/`: Update a book (authenticated).
- **DELETE** `api/books-delete/<id>/`: Delete a book (authenticated).

## Setup:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the server: `python manage.py runserver`
6. Access the API through Postman or any HTTP client.
