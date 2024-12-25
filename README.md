# Library Management System API

A simple API for managing books and members in a library system. The API supports CRUD operations for both books and members.

---

## Features

- Manage Books: Add, edit, delete, and search for books.
- Manage Members: Add, edit, and delete members.
- Authorization via a token.

---

## Prerequisites

- Python 3.9+ installed.
- Flask and SQLite for database and backend.
- Authentication token for secure access.

---

## Setup Instructions

1. Clone the repository:
   `git clone https://github.com/aghasyedi/lms-api.git`
   `cd lmsa-api`

2. Install dependencies:
   `pip install flask`

3. Run the application:
   `python app.py`

---

## API Endpoints

### Books

#### Get all books

**GET** `/books`

- **Query Parameters:**
  - `search` (optional): Filter books by title or author.
- **Headers:**

  - `Authorization`: Required token.

- **Response:**
  [
  {
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "available": true
  }
  ]

#### Add a new book

**POST** `/books`

- **Headers:**

  - `Authorization`: Required token.
  - `Content-Type`: `application/json`

- **Body:**
  {
  "title": "Book Title",
  "author": "Author Name"
  }

- **Response:**
  {
  "message": "Book added successfully"
  }

#### Update a book

**PUT** `/books/<id>`

- **Headers:**

  - `Authorization`: Required token.
  - `Content-Type`: `application/json`

- **Body:**
  {
  "title": "Updated Title",
  "author": "Updated Author"
  }

- **Response:**
  {
  "message": "Book updated successfully"
  }

#### Delete a book

**DELETE** `/books/<id>`

- **Headers:**

  - `Authorization`: Required token.

- **Response:**
  {
  "message": "Book deleted successfully"
  }

---

### Members

#### Get all members

**GET** `/members`

- **Headers:**

  - `Authorization`: Required token.

- **Response:**
  [
  {
  "id": 1,
  "name": "Member Name",
  "email": "member@example.com"
  }
  ]

#### Add a new member

**POST** `/members`

- **Headers:**

  - `Authorization`: Required token.
  - `Content-Type`: `application/json`

- **Body:**
  {
  "name": "Member Name",
  "email": "member@example.com"
  }

- **Response:**
  {
  "message": "Member added successfully"
  }

#### Update a member

**PUT** `/members/<id>`

- **Headers:**

  - `Authorization`: Required token.
  - `Content-Type`: `application/json`

- **Body:**
  {
  "name": "Updated Name",
  "email": "updated@example.com"
  }

- **Response:**
  {
  "message": "Member updated successfully"
  }

#### Delete a member

**DELETE** `/members/<id>`

- **Headers:**

  - `Authorization`: Required token.

- **Response:**
  {
  "message": "Member deleted successfully"
  }

---

## Authentication

All endpoints require a valid `Authorization` header with the value `securetoken`. Update the `AUTH_TOKEN` variable in `app.py` to customize the token.

---

## Database Initialization

The database will be created automatically when you run the application for the first time. It contains two tables:

- `books`: Stores book details.
- `members`: Stores member details.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this code.
