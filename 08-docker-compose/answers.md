# Answer Key: Docker Compose and Multi-Container Apps

## How to Use This Key

The most important idea is that Compose turns many related container settings into one readable project definition.

## Flow-1 Suggested Answers

1. Compose manages multi-container applications in one file.
2. A `compose.yaml` file describes services, ports, volumes, networks, and configuration.
3. `docker compose up -d` creates and starts the services in the background.
4. `docker compose down` stops and removes the project containers and default network.

## Flow-2 Suggested Answers

1. Services are usually on the same Compose network and can resolve each other by service name.
2. Inside a container, `localhost` usually points to the same container.
3. `depends_on` expresses dependency order, but it does not guarantee full readiness.

## Flow-3 Suggested Answers

1. The web app service is `web`.
2. The database service is `db`.
3. Open `http://localhost:5001`.
4. The app uses `db` as the PostgreSQL hostname.

## Flow-4 Reflection Guide

Compose keeps ports, environment variables, volumes, and networks in one place so you do not need to rebuild a long list of manual commands every time.
# Answer Key: Docker Compose and Multi-Container Apps

## Part 1 Suggested Answers

1. Compose manages multi-container applications in one file.
2. A `compose.yaml` file describes services, ports, volumes, networks, and configuration.
3. `docker compose up -d` creates and starts the services in the background.
4. `docker compose down` stops and removes the project containers and default network.

## Part 2 Suggested Answers

1. Services are usually on the same Compose network and can resolve each other by service name.
2. Inside a container, `localhost` usually points to the same container.
3. `depends_on` expresses dependency order, but it does not guarantee full readiness.

## Part 3 Suggested Answers

1. The web app service is `web`.
2. The database service is `db`.
3. Open `http://localhost:5001`.
4. The app uses `db` as the PostgreSQL hostname.

## Part 4 Suggested Answer

Compose puts the app definition in one place, so you do not need to remember separate commands for ports, environment variables, networks, and volumes.
