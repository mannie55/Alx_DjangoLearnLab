# Django Authentication and Post Management System

## Overview
This project implements a user authentication system using Django, including user registration, login, logout, profile update, and post management features. Users can create, update, and manage their posts securely.

## Table of Contents
1. [Authentication Components](#authentication-components)
   - Registration
   - Login
   - Logout
   - Profile Update
2. [Post Management](#post-management)
   - Create Post
   - Update Post
3. [How It Works](#how-it-works)
   - Views
   - Forms
   - Templates
   - Models
   - Signals
4. [User Interaction](#user-interaction)
5. [Testing Guide](#testing-guide)
   - Manual Testing
   - Automated Testing
   - Security Considerations

---

## Authentication Components

### 1. Registration
Users can create an account by providing a username, email, and password. After registration, they are either automatically logged in or redirected to the login page.

### 2. Login
Registered users can log in using their credentials. Successful login grants access to restricted parts of the website.

### 3. Logout
Users can securely log out, ensuring they are no longer authenticated and cannot access restricted areas.

### 4. Profile Update
Allows users to update their personal information such as username, email, and profile picture.

---

## Post Management

### 1. Create Post
Authenticated users can create new posts by providing a title and content. The post is associated with the logged-in user, and only they can edit it.

### 2. Update Post
Users can update their existing posts using the same form used for creating posts. Only the author of a post can edit it, ensuring content integrity and security.

---

## How It Works

### 1. Views
The views handle user interactions such as registration, login, logout, profile updates, post creation, and post updates. Each view is responsible for rendering the appropriate forms, processing user input, and handling redirects.

### 2. Forms
Forms are used to validate and process user data for registration, login, profile updates, and post management. The `PostForm` is used for both creating and updating posts.

### 3. Templates
The templates provide the front-end UI for users to register, log in, update their profile, and manage their posts. Each feature has a corresponding HTML template.

### 4. Models
The `User` model handles basic user information, while a custom `Profile` model extends the `User` model with additional fields such as profile picture and bio. The `Post` model stores post data, including title, content, and author.

### 5. Signals
Django signals automatically create a profile when a new user registers, ensuring that every user has an associated profile.

---

## User Interaction

1. **Registration**: Users visit the registration page to create an account. After registration, they can log in or are automatically authenticated.
2. **Login**: Users log in using their credentials and gain access to restricted areas.
3. **Logout**: Users can log out to terminate their session.
4. **Profile Update**: Users can update their profile information from their profile page.
5. **Create Post**: Authenticated users can create new posts by navigating to the post creation page.
6. **Update Post**: Users can update their own posts by visiting the post edit page. Only the post's author can access the edit functionality.

---

## Testing Guide

### 1. Manual Testing

- **Registration**: Verify that new users can register, and their profiles are created.
- **Login**: Ensure that users can log in with valid credentials.
- **Logout**: Confirm that users are redirected to the home page after logout and can no longer access restricted pages.
- **Profile Update**: Check that users can update their profile and changes are saved properly.
- **Create Post**: Test that authenticated users can create posts, and they appear in the post list.
- **Update Post**: Ensure that only the post author can edit a post and that changes are reflected correctly.

### 2. Automated Testing
Use Django's built-in test framework to create automated tests for each of the authentication and post management features. Focus on edge cases, such as invalid credentials, missing profile data, unauthorized access to post editing, or unauthenticated access to restricted pages.

### 3. Security Considerations
- Ensure that sensitive data (e.g., passwords) is securely handled and never exposed.
- Confirm that only authenticated users can create or update posts and that only the post author can edit their posts.
- Implement CSRF protection for all forms.
- Validate user permissions for each action, preventing unauthorized access to post management features.
