# Nginx CLI Demo

## Goal

This example gives you hands-on practice with essential Docker CLI commands.

## Pre-requisites

- Docker Desktop running
- Port `8080` available on your machine

## Flow

### Step-1: Run the guided script

```powershell
./practice-cli.ps1
```

### Step-2: Open the application

Open:

`http://localhost:8080`

### Step-3: Clean up when finished

```powershell
docker stop cli-nginx-demo
docker rm cli-nginx-demo
```

## Expected Output

You should see:

- An Nginx container start successfully
- `docker ps` showing the running container
- `docker logs` output for the container
- `docker inspect` JSON details
- The Nginx welcome page in the browser

## What You Are Learning

- Starting a container
- Listing containers
- Reading logs
- Inspecting a container
- Cleaning up afterward
