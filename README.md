# SecureHub API

A secure RESTful API built with **Flask** following modern API security practices and the **OWASP API Security Top 10**.

This project was created as both a learning platform and a security portfolio to demonstrate backend development, secure authentication, authorization, and API penetration testing methodology.

---

## Features

### Authentication

- JWT Access Tokens
- JWT Refresh Tokens
- Password Hashing

### Authorization

- Role-Based Access Control (RBAC)
- Object Ownership Validation
- Admin-only Endpoints

### API Key Management

- API Key Generation
- Read / Write Scopes
- API Key Authentication

### Security

- Rate Limiting
- Audit Logging
- Secure Password Storage
- Refresh Token Validation
- Token Type Validation
- Service-to-Service Authentication

---

## Technology Stack

| Component        | Technology                |
|------------------|---------------------------|
| Language         | Python                    |
| Framework        | Flask                     |
| Database         | SQLite                    |
| Authentication   | JWT                       |
| Password Hashing | Werkzeug Security         |
| API Testing      | curl                      |
| Security Testing | OWASP API Security Top 10 |

---

## Project Structure

```text
securehub/

├── api/
├── auth/
├── configuration/
├── middleware/
├── services/
├── repositories/
├── models/
├── database/
├── docs/
├── tests/
├── app.py
└── README.md
```

---

## Architecture

The project follows a layered architecture.

```
Client > Flask Routes > Middleware > Services > Repositories > SQLite Database
```

This separation keeps business logic independent from routing and data access, making the application easier to maintain and test.

---

## Security Controls

- JWT Authentication
- Refresh Tokens 
- Access Tokens 
- RBAC
- Object Ownership Validation
- API Key Authentication
- API Key Scopes
- Rate Limiting
- Audit Logging
- Password Hashing

---

## API Endpoints

### Authentication

```
POST /auth/register
POST /auth/login

```

### Profile

```
GET /api/profile
```

### Users

```
GET /api/users/<id>
PUT /api/users/<id>
```

### Posts

```
GET /api/posts
POST /api/posts
PUT /api/posts/<id>
DELETE /api/posts/<id>
```

### API Keys

```
POST /api/key
GET /api/key
DELETE /api/key/<id>
GET /api/service/profile
```

### Administration

```
GET /api/admin
GET /api/admin/logs
```

---

## Security Assessment

This project is being assessed against the **OWASP API Security Top 10**.

Assessment documentation is available in the `docs/` directory.

Topics include:

- API1 – Broken Object Level Authorization
- API2 – Broken Authentication
- API3 – Broken Object Property Level Authorization
- API4 – Unrestricted Resource Consumption
- API5 – Broken Function Level Authorization
- API6 – Unrestricted Access to Sensitive Business Flows
- API7 – Server-Side Request Forgery (SSRF)
- API8 – Security Misconfiguration
- API9 – Improper Inventory Management
- API10 – Unsafe Consumption of APIs

---

## Project Goals

The objective of this project is to demonstrate:

- Secure REST API development
- Authentication and Authorization
- Object-Oriented Design
- Secure Coding Practices
- API Penetration Testing
- Security Documentation
- Professional Project Structure

---

## Disclaimer

This project is intended for educational purposes and security research within authorized environments only.



