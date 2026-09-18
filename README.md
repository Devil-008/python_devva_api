# User Management REST API (DEVAA Baseline Repository)

A baseline Python Flask REST API for User Management. This repository is structured cleanly to serve as the starting state for evaluating AI coding agents (such as **DEVAA**).

---

## 🎯 Purpose

This repository represents the **baseline version** of the User Management API **before** email format validation is added. It provides a complete, runnable, and fully-tested starting point.

An AI development agent (DEVAA) will use this baseline repo to:
1. Analyze the existing code architecture.
2. Locate the user registration endpoint (`POST /users`) and service logic (`app/services/user_service.py`).
3. Implement email format validation.
4. Add unit tests for email format validation.
5. Run the pytest test suite to verify changes.
6. Create a feature branch and pull request.

---

## 📂 Project Architecture

The project follows clean architecture principles, separating models, services, controllers/routes, configuration, and unit tests:

```text
.
├── app/
│   ├── __init__.py          # Application Factory (create_app) & global error handlers
│   ├── extensions.py        # SQLAlchemy extension instance
│   ├── models.py            # User database model definition
│   ├── routes/
│   │   └── users.py         # REST API endpoints (Flask Blueprint)
│   └── services/
│       └── user_service.py  # Business logic & database operations
├── tests/
│   ├── conftest.py          # Pytest fixtures (in-memory database, test client)
│   └── test_users.py        # Baseline unit test suite
├── config.py                # Configuration classes (Dev, Test, Prod)
├── run.py                   # Application entry point
├── requirements.txt         # Python package dependencies
├── .env.example             # Environment variable template
├── .gitignore               # Standard git ignore rules
└── README.md                # Project documentation
```

---

## 🛠️ Data Model

### `User` Entity
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Primary key, auto-incrementing |
| `name` | String(100) | Full name (Required) |
| `email` | String(120) | Unique email address (Required) |
| `password` | String(255) | Hashed password (Required) |
| `created_at` | DateTime | Timestamp when user was created |

---

## 🚀 Setup & Local Execution

### Prerequisites
- Python 3.9+
- `pip`

### 1. Environment Setup

Clone the repository and create a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

### 4. Run the Application

```bash
python run.py
```
The API server will start on `http://127.0.0.1:5000`.

---

## 📡 API Endpoints

| Method | Endpoint | Description | Status Codes |
| :--- | :--- | :--- | :--- |
| `POST` | `/users` | Register / Create a new user | `201 Created`, `400 Bad Request`, `409 Conflict` |
| `GET` | `/users` | Retrieve list of all users | `200 OK` |
| `GET` | `/users/<id>` | Retrieve a single user by ID | `200 OK`, `404 Not Found` |
| `DELETE` | `/users/<id>` | Delete a user by ID | `200 OK`, `404 Not Found` |

### Example Request (`POST /users`)
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "password": "secretpassword"
}
```

### Example Response (`201 Created`)
```json
{
  "id": 1,
  "name": "Jane Doe",
  "email": "jane@example.com",
  "created_at": "2026-09-08T17:20:00+00:00"
}
```

---

## 🧪 Running Unit Tests

The test suite uses `pytest` with an in-memory SQLite database (`sqlite:///:memory:`).

To execute all tests:

```bash
pytest -v
```

### Expected Test Output
All baseline tests should pass out of the box:
- `test_create_user_success`
- `test_create_user_non_standard_email_accepted`
- `test_create_user_missing_required_fields`
- `test_create_user_duplicate_email`
- `test_get_all_users`
- `test_get_user_by_id`
- `test_delete_user`

---

## ⚠️ Important Baseline Note

Email format validation is **intentionally NOT implemented** in this baseline version. The `POST /users` endpoint accepts any non-empty string as an email. Adding regex or `email-validator` format validation is reserved as the target task for DEVAA evaluation.

## Changelog & Recent Updates

### Allow user to update their name, email, password

As a registered user, I want to update my name, email address, and password so that I can keep my account information up to date.

Description

The existing User Management API allows users to create and retrieve user accounts.

Add an API endpoint that allows an existing user to update their profile information.

The user should be able to update their name, email, password, or any combination of these fields without having to provide all three fields.

The implementation should follow the existing project architecture, database access patterns, validation approach, and API response conventio

**Acceptance Criteria:**
AC1 — Update name

When a valid user ID and a new name are provided:

• The user's name must be updated successfully.
• The updated value must be persisted in the database.
• The API must return the updated user information.

AC2 — Update email

When a valid user ID and a valid new email address are provided:

• The user's email must be updated successfully.
• The updated email must be persisted i

## Changelog & Recent Updates

### Allow user to update their name, email, password

As a registered user, I want to update my name, email address, and password so that I can keep my account information up to date.

Description

The existing User Management API allows users to create and retrieve user accounts.

Add an API endpoint that allows an existing user to update their profile information.

The user should be able to update their name, email, password, or any combination of these fields without having to provide all three fields.

The implementation should follow the existing project architecture, database access patterns, validation approach, and API response conventio

**Acceptance Criteria:**
AC1 — Update name

When a valid user ID and a new name are provided:

• The user's name must be updated successfully.
• The updated value must be persisted in the database.
• The API must return the updated user information.

AC2 — Update email

When a valid user ID and a valid new email address are provided:

• The user's email must be updated successfully.
• The updated email must be persisted i

## Changelog & Recent Updates

### Allow user to update their name, email, password

As a registered user, I want to update my name, email address, and password so that I can keep my account information up to date.

Description

The existing User Management API allows users to create and retrieve user accounts.

Add an API endpoint that allows an existing user to update their profile information.

The user should be able to update their name, email, password, or any combination of these fields without having to provide all three fields.

The implementation should follow the existing project architecture, database access patterns, validation approach, and API response conventio

**Acceptance Criteria:**
AC1 — Update name

When a valid user ID and a new name are provided:

• The user's name must be updated successfully.
• The updated value must be persisted in the database.
• The API must return the updated user information.

AC2 — Update email

When a valid user ID and a valid new email address are provided:

• The user's email must be updated successfully.
• The updated email must be persisted i
