# Security Architecture

## Overview

SecureHub API was designed using a defense-in-depth approach, where multiple security controls work together to protect the application.

Instead of relying on a single security mechanism, authentication, authorization, validation, and monitoring are implemented at different layers of the application.

---

# Security Model

```
                 Client
                    │
                    ▼
           Authentication Layer
                    │
                    ▼
           Authorization Layer
                    │
                    ▼
             Business Logic
                    │
                    ▼
              Database Layer
                    │
                    ▼
               Audit Logging
```

A request must successfully pass every layer before protected resources are accessed.

---

# Authentication

## JWT Authentication

The API uses JSON Web Tokens (JWT) for stateless authentication.

Two token types are implemented:

- Access Token
- Refresh Token

### Access Token

Purpose:

- Authenticate requests to protected API endpoints.

Characteristics:

- Short-lived
- Sent using the Authorization header
- Required for protected resources

Example

```
Authorization: Bearer <access_token>
```

---

## Refresh Token

Purpose:

Generate a new Access Token after expiration.

Security Controls:

- Cannot directly access protected endpoints.
- Validated separately from Access Tokens.
- Stored in the database for revocation.

Token type validation prevents Refresh Tokens from being used as Access Tokens.

---

# Password Security

Passwords are never stored in plaintext.

Security measures:

- Werkzeug password hashing
- Password verification using secure comparison
- Plaintext passwords are discarded after verification

---

# Authorization

Authentication identifies the user.

Authorization determines what the user is allowed to do.

SecureHub implements multiple authorization mechanisms.

---

## Role-Based Access Control (RBAC)

Roles include:

- User
- Admin

Administrative endpoints require administrator privileges.

Examples:

```
GET /api/admin
GET /api/admin/logs
```

---

## Object Ownership Validation

Users may only modify resources they own.

Example:

```
User A

↓

PUT /api/posts/15

↓

Verify:

post.user_id == current_user.id
```

This prevents Broken Object Level Authorization (OWASP API1).

---

# API Key Authentication

The application supports API Keys for service-to-service communication.

Each API Key is assigned a scope.

Scopes include:

- Read
- Write
- Admin

Every protected endpoint verifies that the presented API Key contains the required permissions before allowing access.

---

# Rate Limiting

Rate limiting is implemented to reduce abuse.

Objectives:

- Reduce brute-force attacks
- Prevent API abuse
- Mitigate denial-of-service attempts

Rate limits are enforced before business logic executes.

---

# Audit Logging

Security-relevant events are recorded.

Examples:

- Login
- API Key creation
- Administrative actions
- Resource modification
- Resource deletion

Audit logs support:

- Incident response
- Security investigations
- Accountability

---

# Input Validation

Incoming requests are validated before processing.

Examples:

- Required fields
- Missing JSON
- Invalid identifiers
- Authorization headers

Invalid requests are rejected before reaching business logic.

---

# Secure Design Principles

SecureHub follows several security design principles.

- Least Privilege
- Defense in Depth
- Separation of Concerns
- Fail Secure
- Secure Defaults

---

# OWASP API Security

The project is continuously assessed against the OWASP API Security Top 10.

Current assessment includes:

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

Assessment results are documented separately in:

```
docs/PENTEST.md
```