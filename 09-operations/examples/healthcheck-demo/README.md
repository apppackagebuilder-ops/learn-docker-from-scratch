# Health Check Demo

## Goal

This example shows the difference between a container that is running and a container that is healthy.

## Pre-requisites

- Docker Desktop running
- Port `5002` available on your machine

## Flow

### Step-1: Build the image

```powershell
docker build -t healthcheck-demo .
```

### Step-2: Run the container

```powershell
docker run -d -p 5002:5000 --name healthcheck-demo healthcheck-demo
```

### Step-3: Open the health endpoint

Open:

`http://localhost:5002/health`

### Step-4: Inspect the container

```powershell
docker inspect healthcheck-demo
```

## Expected Output

You should see a healthy JSON response from `/health`.

The container inspection should show health information once checks begin running.

## What You Are Learning

- How `HEALTHCHECK` works
- How to inspect container health status
- Why logs and health are both useful for operations
