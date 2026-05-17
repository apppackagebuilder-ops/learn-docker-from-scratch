# Installation Verification Example

## Goal

This example verifies that Docker is installed correctly and working on your machine.

## Pre-requisites

- Docker Desktop installed
- Docker Desktop started

## Flow

### Step-1: Run the verification script

```powershell
./check-docker-installation.ps1
```

## Expected Output

You should see:

- Docker version information
- Docker environment information
- A successful `hello-world` message
- A list of images including `hello-world`
- A list of containers including the stopped `hello-world` container

## What You Are Learning

- How to verify Docker installation
- How to verify the Docker engine is responding
- How to confirm the machine can run containers
