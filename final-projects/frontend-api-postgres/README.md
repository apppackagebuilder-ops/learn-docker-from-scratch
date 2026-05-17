# Frontend, API, and PostgreSQL Project

## Goal

This project is a realistic full-stack Docker example.

You will run three services together:

- `frontend`: static web UI served by Nginx
- `api`: Flask API
- `db`: PostgreSQL database

## What You Learn

- Running a frontend, backend, and database together
- Using Docker Compose for a multi-service app
- Reverse proxying API requests from the frontend
- Using PostgreSQL with a persistent volume
- Reading how services connect to each other

## Pre-requisites

- Docker Desktop running
- Port `8092` available on your machine
- Port `8093` available on your machine

## Project Files

- `frontend/`: static UI and Nginx config
- `api/`: Flask API code
- `database/init.sql`: initial database schema and seed data
- `compose.yaml`: starts the full stack

## Flow

### Step-1: Start the project

```powershell
docker compose up --build -d
```

### Step-2: Open the frontend

Open:

`http://localhost:8092`

### Step-3: Check the direct API endpoint

Open:

`http://localhost:8093/api/products`

### Step-4: Stop the project when finished

```powershell
docker compose down
```

## Expected Output

- The frontend page should load successfully
- The frontend should display product data from the API
- The API endpoint should return seeded JSON data from PostgreSQL

## What To Notice

- The browser normally needs only the frontend URL
- The frontend proxies API requests to the backend
- The backend talks to PostgreSQL using service-to-service networking
- Database data is stored in the `storedata` named volume
