# Microservices Demo

## Goal

This project is an introduction to a tiny microservices-style setup.

You will run two Flask services together:

- `product-service`
- `gateway-service`

## What You Learn

- Building more than one custom image
- Running multiple services with Compose
- Service-to-service communication
- Using service names on the internal network

## Pre-requisites

- Docker Desktop running
- Port `8090` available on your machine

## Project Files

- `product-service/`: product data service
- `gateway-service/`: gateway service
- `compose.yaml`: starts both services

## Flow

### Step-1: Start the project

```powershell
docker compose up --build -d
```

### Step-2: Open the application

Open:

`http://localhost:8090`

### Step-3: Stop the project when finished

```powershell
docker compose down
```

## Expected Output

- The gateway should return JSON
- The gateway should call `product-service` using the service name on the Docker network

## What To Notice

- Each service has its own Dockerfile
- Compose builds both services
- The gateway uses `product-service` instead of a hard-coded IP address
