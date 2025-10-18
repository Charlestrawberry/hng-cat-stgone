# hng-cat-stgone

# Stage Zero Backend Task - /me Endpoint

## Overview

This project implements a RESTful API endpoint that returns user profile info and a random cat fact.

## Endpoint

**GET** `/me`

### Response

```json
{
  "status": "success",
  "user": {
    "email": "your_email@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-17T12:00:00.000Z",
  "fact": "Cats sleep for 70% of their lives."
}
```
