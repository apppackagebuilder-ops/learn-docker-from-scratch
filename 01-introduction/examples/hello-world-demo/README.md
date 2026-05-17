# Hello World Demo

## Goal

This is the smallest possible Docker practice example.

It helps you understand the first Docker flow:

1. Docker finds an image
2. Docker runs a container
3. The container prints output
4. The container stops

## Pre-requisites

- Docker Desktop installed
- Docker Desktop running

## Flow

### Step-1: Run the helper script

```powershell
./run-hello-world.ps1
```

### Step-2: Run the raw command if you want to practice manually

```powershell
docker run hello-world
```

### Step-3: List all containers

```powershell
docker ps -a
```

## Expected Output

You should see:

- A Docker success message from the `hello-world` container
- A stopped `hello-world` container in `docker ps -a`

## What You Are Learning

- Docker can pull an image automatically
- A container can do a short task and stop
- Stopped containers can still be listed later
