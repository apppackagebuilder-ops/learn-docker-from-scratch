# PostgreSQL and pgAdmin

## Goal

This project helps you practice a real multi-container setup.

You will run:

- PostgreSQL as the database
- pgAdmin as the browser-based admin tool

## What You Learn

- Running more than one container together
- Using Docker Compose
- Using environment variables
- Keeping database data in a volume
- Connecting one service to another

## Pre-requisites

- Docker Desktop running
- Port `8089` available on your machine

## Project Files

- `compose.yaml`: starts PostgreSQL and pgAdmin
- `.env.example`: sample environment values

## Flow

### Step-1: Start the project

```powershell
docker compose up -d
```

### Step-2: Open pgAdmin

Open:

`http://localhost:8089`

### Step-3: Log in to pgAdmin

- Email: `admin@example.com`
- Password: `admin123`

### Step-4: Register the PostgreSQL server

Use:

- Host: `db`
- Port: `5432`
- Database: `appdb`
- Username: `appuser`
- Password: `apppass`

### Step-5: Stop the project when finished

```powershell
docker compose down
```

## Expected Output

- pgAdmin should load in the browser
- PostgreSQL should be reachable from pgAdmin using `db` as the hostname
- Database data should survive normal stop and start cycles because of the named volume
