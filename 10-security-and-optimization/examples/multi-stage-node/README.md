# Multi-Stage Node Example

## Goal

This example shows how a multi-stage Dockerfile can produce a cleaner runtime image.

## Pre-requisites

- Docker Desktop running
- Port `3000` available on your machine

## Flow

### Step-1: Build the image

```powershell
docker build -t multi-stage-node-demo .
```

### Step-2: Run the container

```powershell
docker run -d -p 3000:3000 --name multi-stage-node-demo multi-stage-node-demo
```

### Step-3: Open the application

Open:

`http://localhost:3000`

## Expected Output

You should see a JSON response from the Node.js app.

## What You Are Learning

- How multiple `FROM` stages work
- Why the runtime image can be smaller than the build environment
- How a non-root user can be used in the final image
