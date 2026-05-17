# Good Python Service Example

## Goal

This example bundles several Docker best practices into one small service.

## What It Demonstrates

- A small trusted base image
- Dependency installation before copying the full app
- `.dockerignore` to keep the build context clean
- Environment variables for configuration
- Logging to standard output
- A health check endpoint
- Running as a non-root user
- A Compose file for easy local startup

## Pre-requisites

- Docker Desktop running
- Port `8010` available on your machine

## Flow

### Step-1: Start the example

```powershell
docker compose up --build -d
```

### Step-2: Open the application

Open:

`http://localhost:8010`

### Step-3: Open the health endpoint

Open:

`http://localhost:8010/health`

### Step-4: Stop the example when finished

```powershell
docker compose down
```

## Expected Output

- The main endpoint should return JSON with the service name, environment, and message
- The health endpoint should return a healthy response
