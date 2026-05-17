# Network Demo

## Goal

This example shows how two containers on the same network can reach each other by name.

## Pre-requisites

- Docker Desktop running

## Flow

### Step-1: Start the example

```powershell
docker compose up -d
```

### Step-2: Verify the containers are running

You should see these containers:

- `network-demo-web`
- `network-demo-toolbox`

### Step-3: Connect to the toolbox container

```powershell
docker exec -it network-demo-toolbox sh
```

### Step-4: Test the web container by name

Inside the toolbox shell, install curl and request the web service.

## Expected Output

You should be able to contact the web service by container or service name because both services share the same Docker network.

## What You Are Learning

- How Compose creates a shared network
- How containers on the same network can reach each other by name
