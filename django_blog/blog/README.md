# Django Authentication System

## Overview
This project implements a user authentication system using Django. It includes features such as user registration, login, logout, profile updates, and password management.

## Table of Contents
1. [Authentication Components](#authentication-components)
   - Registration
   - Login
   - Logout
   - Profile Update
   - Password Reset/Change
2. [How It Works](#how-it-works)
   - Views
   - Forms
   - Templates
   - Models
   - Signals
3. [User Interaction](#user-interaction)
4. [Testing Guide](#testing-guide)
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

## How It Works

### 1. Views
The views handle user interactions such as registration, login, logout, and profile updates. Each view is responsible for rendering the appropriate forms, processing user input, and handling redirects.

### 2. Forms
Forms are used to validate and process user data for registration, login, and profile updates. These forms interact with both Django’s built-in `User` model and the custom `Profile` model.

### 3. Templates
The templates provide the front-end UI for users to register, log in, update their profile, and reset their password. Each feature has a corresponding HTML template.

### 4. Models
The `User` model handles basic user information, while a custom `Profile` model extends the `User` model with additional fields such as profile picture and bio.

### 5. Signals
Django signals automatically create a profile when a new user registers, ensuring that every user has an associated profile.

---

## User Interaction

1. **Registration**: Users visit the registration page to create an account. After registration, they can log in or are automatically authenticated.
2. **Login**: Users log in using their credentials and gain access to restricted areas.
3. **Logout**: Users can log out to terminate their session.
4. **Profile Update**: Users can update their profile information from their profile page.

---

## Testing Guide

### 1. Manual Testing

- **Registration**: Verify that new users can register, and their profiles are created.
- **Login**: Ensure that users can log in with valid credentials.
- **Logout**: Confirm that users are redirected to the home page after logout and can no longer access restricted pages.
- **Profile Update**: Check that users can update their profile and changes are saved properly.

### 2. Automated Testing
Use Django's built-in test framework to create automated tests for each of the authentication features. Focus on edge cases, such as invalid credentials, missing profile data, or unauthenticated access to restricted pages.

### 3. Security Considerations
- Ensure that sensitive data (e.g., passwords) is securely handled and never exposed.
- Confirm that only authenticated users can access restricted content or profile updates.
- Implement CSRF protection for all forms.
