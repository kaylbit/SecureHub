# SecureHub API Documentation

## Overview

SecureHub is a RESTful API that demonstrates secure API development using Flask. The application implements JWT authentication, Role-Based Access Control (RBAC), API key management, and secure CRUD operations.

**Base URL**

```text
http://127.0.0.1:5000
```

---

# Authentication

Most endpoints require a JWT access token.

Include the token in the request header:

```http
Authorization: Bearer <ACCESS_TOKEN>
```

---

# Authentication Endpoints

| Method | Endpoint         | Description                               | Authentication |
| ------ | ---------------- | ----------------------------------------- | -------------- |
| POST   | `/auth/register` | Register a new user                       |  No            |
| POST   | `/auth/login`    | Authenticate a user and return JWT tokens |  No            |

---

# User Endpoints

| Method | Endpoint               | Description                               | Authentication |
| ------ | ---------------------- | ----------------------------------------- | -------------- |
| GET    | `/api/profile`         | Retrieve the authenticated user's profile | Required       |
| GET    | `/api/service/profile` | Retrieve service profile information      | Required       |
| GET    | `/api/users/<id>`      | Retrieve a user by ID                     | Required       |
| PUT    | `/api/users/<id>`      | Update the authenticated user's username  | Required       | 

---

# Post Endpoints

| Method | Endpoint          | Description          | Authentication |
| ------ | ----------------- | -------------------- | -------------- |
| GET    | `/api/posts`      | Retrieve all posts   | Required       |
| POST   | `/api/posts`      | Create a new post    | Required       |
| PUT    | `/api/posts/<id>` | Update an owned post | Required       |
| DELETE | `/api/posts/<id>` | Delete an owned post | Required       |

---

# API Key Endpoints

| Method | Endpoint        | Description                                | Authentication |
| ------ | --------------- | ------------------------------------------ | -------------- |
| GET    | `/api/key`      | Retrieve the authenticated user's API keys | Required       |
| POST   | `/api/key`      | Create a new API key                       | Required       |
| DELETE | `/api/key/<id>` | Delete an owned API key                    | Required       |

---

# Administrator Endpoints

These endpoints require the **Administrator** role.

| Method | Endpoint          | Description             | Authentication |
| ------ | ----------------- | ----------------------- | -------------- |
| GET    | `/api/admin`      | Administrator dashboard | Admin          |
| GET    | `/api/admin/logs` | Retrieve audit logs     | Admin          |

---

# Response Codes

| Status Code               | Description                                           |
| ------------------------- | ----------------------------------------------------- |
| 200 OK                    | Request completed successfully                        |
| 201 Created               | Resource created successfully                         |
| 400 Bad Request           | Invalid request data                                  |
| 401 Unauthorized          | Authentication failed or token is invalid             |
| 403 Forbidden             | User lacks permission to perform the requested action |
| 404 Not Found             | Requested resource does not exist                     |
| 429 Too Many Requests     | Rate limit exceeded                                   |
| 500 Internal Server Error | Unexpected server error                               |

---

# Security Features

SecureHub implements the following security controls:

* JWT-based authentication
* Access and Refresh Tokens
* Role-Based Access Control (RBAC)
* Object Ownership Authorization
* API Key Management
* Login Rate Limiting
* Audit Logging
* Input Validation
* Password Hashing

---

# Authorization Model

| Resource               | User           | Administrator       |
| ---------------------- | ---------------| ------------------- |
| View own profile       | Allowed        | Allowed             |
| Update own username    | Allowed        | Allowed             |
| Create posts           | Allowed        | Allowed             |
| Update own posts       | Allowed        | Allowed             |
| Delete own posts       | Allowed        | Allowed             |
| Create API keys        | Allowed        | Allowed             |
| Delete own API keys    | Allowed        | Allowed             |
| Access admin dashboard | Not allowed    | Allowed             |
| View audit logs        | Not allowed    | Allowed             |

---

# Penetration Testing

SecureHub has been assessed using the **OWASP API Security Top 10 (2023)** methodology.

The penetration testing reports are available in the `pentest/` directory.
