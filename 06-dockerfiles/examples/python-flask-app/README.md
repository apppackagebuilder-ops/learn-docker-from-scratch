# Python Flask App Example

## Goal

This example shows how a Dockerfile builds and runs a simple Python Flask application.

## Pre-requisites

- Docker Desktop running
- Port `5000` available on your machine

## Flow

### Step-1: Build the Docker image

```powershell
docker build -t flask-demo .
```

### Step-2: Run the container

```powershell
docker run -d -p 5000:5000 --name flask-demo-app flask-demo
```

### Step-3: Access the application

Open:

`http://localhost:5000`

### Step-4: Review logs if needed

```powershell
docker logs flask-demo-app
```

## Expected Output

You should see a JSON response from the Flask app.

## What You Are Learning

- How a Dockerfile becomes an image
- How dependencies are installed during build
- How the container starts the app with `CMD`
