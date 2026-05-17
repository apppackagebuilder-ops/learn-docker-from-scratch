# Simple Web App

## Goal

This is the simplest final project in the course.

You will serve a static website using Nginx in Docker.

## What You Are Learning

- Reading a Dockerfile
- Building an image
- Starting a project with Compose
- Opening the app in a browser
- Rebuilding after changing a file

## Pre-requisites

- Docker Desktop running
- Port `8088` available on your machine

## Project Files

- `Dockerfile`: builds the image
- `compose.yaml`: starts the container
- `site/index.html`: page content

## Flow

### Step-1: Start the project

```powershell
docker compose up --build -d
```

### Step-2: Open the application

Open:

`http://localhost:8088`

### Step-3: Stop the project when finished

```powershell
docker compose down
```

## Expected Output

You should see the sample web page from `site/index.html`.

## What To Notice

- This project uses one container only
- Nginx serves static files
- Port `8088` on your machine maps to port `80` in the container
