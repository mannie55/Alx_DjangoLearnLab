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
- **ListView**: 
    - Retrieves all books with filtering, searching, and ordering capabilities.
    - **Filter**: Only books authored by the currently authenticated user.
    - **Search**: Search by `title` and `author`.
    - **Order**: Order by `title` or `publication_year`. Default is `title`.
- **CreateView**: 
    - Allows authenticated users to create new books with validation for publication year.
- **DetailView**: 
    - Retrieves a specific book by its ID.
- **UpdateView**: 
    - Allows updating an existing book with validation for publication year.
- **DeleteView**: 
    - Allows deletion of a book by its ID.
## Permissions:
- `IsAuthenticatedOrReadOnly`: Allows unauthenticated users to read data, while authenticated users can modify it.
- `IsAuthenticated`: Allows only authenticated users to modify data.

## Token Authentication:
1. Obtain a token by sending a POST request with username and password to `/api/token/`.
2. Include the token in the `Authorization` header of any request requiring authentication.
   - Example:
     ```
     Authorization: Token your_token_here
     ```

## Endpoints:
- **POST** `api/authors/`: Create a new author.
- **GET** `api/authors/`: Retrieve all authors.
- **GET** `api/books/`: Retrieve all books.
- **POST** `api/books/create/`: Create a new book (authenticated).
- **GET** `api/books/<id>/`: Retrieve a specific book.
- **PUT** `api/books/update/<id>/`: Update a book (authenticated).
- **DELETE** `api/books/delete/<id>/`: Delete a book (authenticated).

## Setup:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the server: `python manage.py runserver`
6. Access the API through Postman or any HTTP client.
