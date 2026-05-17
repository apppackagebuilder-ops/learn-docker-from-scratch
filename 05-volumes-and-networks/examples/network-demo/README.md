# Network Demo

## Purpose

This example shows two services attached to the same Compose network.

## Run

```powershell
docker compose up -d
```

## Expected Output

You should see two containers start:

- `network-demo-web`
- `network-demo-toolbox`

You can then use the toolbox container to test network communication.

Example:

```powershell
docker exec -it network-demo-toolbox sh
```

Inside the shell, install curl and request the web service.

## What You Are Learning

- How Compose creates a shared network
- How containers on the same network can reach each other by name
