# Microservices Demo

## Goal

This project is your introduction to a tiny microservices-style setup.

You will run two Flask services together:

- `product-service`, which returns product data
- `gateway-service`, which calls `product-service` and returns a combined response

## What You Learn

This project helps you practice:

- Building more than one custom image
- Running multiple services with Compose
- Service-to-service communication
- Using service names on the internal Docker network

## Read the Project Structure First

Before running it, look at the folders:

- `product-service/`
- `gateway-service/`
- `compose.yaml`

Notice that each service has its own:

- Application code
- `requirements.txt`
- Dockerfile

That is a common pattern in small service-based systems.

## Step-by-Step: Start the Project

Open a terminal in this folder and run:

```powershell
docker compose up --build -d
```

What this does:

1. Reads `compose.yaml`
2. Builds the image for `product-service`
3. Builds the image for `gateway-service`
4. Creates the project network
5. Starts both containers

## Test the Project

Open:

`http://localhost:8090`

Expected result:

- The gateway returns JSON
- The gateway talks to `product-service` using `http://product-service:5000`

## The Most Important Concept Here

The gateway does not need a hard-coded IP address.

Because both services are in the same Compose project, the gateway can use the service name:

- `product-service`

That is one of the key ideas behind Docker networking in multi-service apps.

## Stop the Project

```powershell
docker compose down
```

## Beginner Practice Tasks

1. Change the product list in `product-service/app.py`
2. Rebuild the stack
3. Reload the browser
4. Confirm the new data appears
5. Add a new endpoint to one service
6. Call it from the browser or another service

## Questions To Ask Yourself

1. Which service talks directly to the browser?
2. Which service provides the raw product data?
3. Why does the gateway use `product-service` instead of `localhost`?
4. Why does each service have its own Dockerfile?
