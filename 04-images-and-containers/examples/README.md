# Images and Containers Example

## Goal

This example helps you see the difference between an image and a running container.

It also shows how static files can be served through an Nginx container.

## Pre-requisites

- Docker Desktop running
- Port `8083` available on your machine

## Flow

### Step-1: Run the example script

```powershell
./run-example.ps1
```

### Step-2: Open the application

Open:

`http://localhost:8083`

### Step-3: Stop and remove the container when finished

```powershell
docker stop static-demo
docker rm static-demo
```

## Expected Output

You should see:

- A container named `static-demo` start successfully
- A message telling you to open `http://localhost:8083`
- The static HTML page in the browser

## What You Are Learning

- How an image becomes a running container
- How a bind mount can supply files to the container
- How port mapping exposes the app to the browser
