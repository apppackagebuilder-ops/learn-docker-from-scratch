# Web and Database Compose Example

## Purpose

This example shows a Flask app and PostgreSQL working together through Docker Compose.

## Run

```powershell
docker compose up --build -d
```

## Expected Output

Open:

`http://localhost:5001`

You should see JSON from the Flask app.

That response confirms:

- The web service started
- The database service started
- The web service can connect to PostgreSQL

## What You Are Learning

- Multi-container Compose setup
- Service-to-service communication
- Environment-based database configuration
