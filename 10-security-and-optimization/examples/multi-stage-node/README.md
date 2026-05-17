# Multi-Stage Node Example

## Purpose

This example shows how a multi-stage Dockerfile can produce a cleaner runtime image.

## Build

```powershell
docker build -t multi-stage-node-demo .
```

## Run

```powershell
docker run -d -p 3000:3000 --name multi-stage-node-demo multi-stage-node-demo
```

## Expected Output

Open:

`http://localhost:3000`

You should see a JSON response from the Node.js app.

## What You Are Learning

- How multiple `FROM` stages work
- Why the runtime image can be smaller than the build environment
- How a non-root user can be used in the final image
