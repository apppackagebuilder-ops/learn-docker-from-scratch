# Health Check Demo

## Purpose

This example shows the difference between a container that is merely running and a container that is healthy.

## Build

```powershell
docker build -t healthcheck-demo .
```

## Run

```powershell
docker run -d -p 5002:5000 --name healthcheck-demo healthcheck-demo
```

## Expected Output

Open:

`http://localhost:5002/health`

You should see a healthy JSON response.

You can also inspect the container health status with:

```powershell
docker inspect healthcheck-demo
```

## What You Are Learning

- How `HEALTHCHECK` works
- How to inspect health status
- Why logs and health are both useful
