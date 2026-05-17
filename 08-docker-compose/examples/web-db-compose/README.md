# Web and Database Compose Example

## Goal

This example shows a Flask app and PostgreSQL working together through Docker Compose.

## Pre-requisites

- Docker Desktop running
- Port `5001` available on your machine

## Flow

### Step-1: Start the stack

```powershell
docker compose up --build -d
```

### Step-2: Verify services are running

```powershell
docker compose ps
```

### Step-3: Open the application

Open:

`http://localhost:5001`

### Step-4: View logs if needed

```powershell
docker compose logs -f
```

### Step-5: Stop the stack when finished

```powershell
docker compose down
```

## Expected Output

You should see JSON from the Flask app.

That response confirms:

- The web service started
- The database service started
- The web service can connect to PostgreSQL

## What You Are Learning

- Multi-container Compose setup
- Service-to-service communication
- Environment-based database configuration
