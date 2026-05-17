# Environment and Startup Demo

## Goal

This example shows how environment variables, `CMD`, and `ENTRYPOINT` change container behavior.

## Pre-requisites

- Docker Desktop running

## Flow

### Step-1: Build the image

```powershell
docker build -t env-demo .
```

### Step-2: Run with defaults

```powershell
docker run --rm env-demo
```

### Step-3: Run with custom values

```powershell
docker run --rm -e APP_NAME=CourseApp env-demo --mode production
```

## Expected Output

You should see lines that print:

- The application name
- The application environment
- The selected mode

Those values change depending on the environment variables and startup arguments you pass.

## What You Are Learning

- How runtime configuration changes behavior
- How `CMD` supplies defaults
- How `ENTRYPOINT` fixes the main executable
