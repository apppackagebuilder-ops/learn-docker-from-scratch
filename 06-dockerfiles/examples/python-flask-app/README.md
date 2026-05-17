# Python Flask App Example

## Purpose

This example teaches how a Dockerfile builds a simple Python web application.

## Build

```powershell
docker build -t flask-demo .
```

## Run

```powershell
docker run -d -p 5000:5000 --name flask-demo-app flask-demo
```

## Expected Output

Open:

`http://localhost:5000`

You should see a JSON response from the Flask app.

## What You Are Learning

- How a Dockerfile becomes an image
- How dependencies are installed during build
- How the container starts the app with `CMD`
