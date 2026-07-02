# Architecture

## Overview

SecureHub API follows a layered architecture to separate responsibilities and improve maintainability, scalability, and security.

Each layer has a single responsibility.

```
                Client
                  │
                  ▼
           Flask API Routes
                  │
                  ▼
            Authentication
            Authorization
             Middleware
                  │
                  ▼
             Service Layer
                  │
                  ▼
          Repository Layer
                  │
                  ▼
           SQLite Database
```

---

# Layers

## 1. API Layer

Directory:

```
api/
auth/
```

Responsibilities:

- Receive HTTP requests
- Validate request format
- Return HTTP responses
- Call the appropriate service

The API layer should not contain business logic.

---

## 2. Middleware Layer

Directory:

```
middleware/
```

Responsibilities:

- JWT Authentication
- API Key Authentication
- Rate Limiting
- Role Verification
- Token Validation

The middleware authenticates requests before they reach the application logic.

---

## 3. Service Layer

Directory:

```
services/
```

Responsibilities:

- Business Logic
- Authorization Decisions
- Validation
- Audit Logging

Examples:

- Create Post
- Generate API Key
- Issue JWT
- Verify Permissions

---

## 4. Repository Layer

Directory:

```
repositories/
```

Responsibilities:

- Database Queries
- Data Retrieval
- Data Persistence

Repositories isolate SQL from the rest of the application.

---

## 5. Database Layer

Directory:

```
database/
```

SQLite stores:

- Users
- Posts
- API Keys
- Refresh Tokens
- Audit Logs
- Rate Limiting Data

---

# Authentication Flow

```
        Client
          │
          ▼
    POST /auth/login
          │
          ▼
  Password Verification
          │
          ▼
    JWT Access Token
    JWT Refresh Token
          │
          ▼
  Client Stores Tokens
          │
          ▼
   Protected Endpoint
          │
          ▼
     JWT Middleware
          │
          ▼
     Service Layer
          │
          ▼
      Repository
          │
          ▼
       Response
```

---

# Authorization Flow

```
        JWT
         │
         ▼
   Extract User ID
         │
         ▼
Retrieve Current User
         │
         ▼
    Verify Role
         │
         ▼
  Verify Ownership
         │
         ▼
    Execute Request
```

---

# Design Principles

The project follows the following software engineering principles:

- Separation of Concerns
- Single Responsibility Principle (SRP)
- Layered Architecture
- Reusable Services
- Repository Pattern
- Defense in Depth

---

# Security Architecture

Security is enforced through multiple layers.

    Authentication
         │
         ▼
    Authorization
         │
         ▼
    Input Validation
         │
         ▼
    Rate Limiting
         │
         ▼
    Audit Logging
         │
         ▼
      Database

A request must successfully pass every layer before accessing protected resources.