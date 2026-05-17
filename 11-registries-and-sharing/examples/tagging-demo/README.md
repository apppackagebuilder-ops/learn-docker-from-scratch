# Tagging Demo

## Goal

This example gives you a small image so you can practice build, tag, and push commands.

## Pre-requisites

- Docker Desktop running
- A Docker Hub account if you want to push the image

## Flow

### Step-1: Build the image

```powershell
docker build -t registry-demo .
```

### Step-2: Tag the image

```powershell
docker tag registry-demo your-dockerhub-name/registry-demo:1.0.0
```

### Step-3: Push the image

```powershell
docker push your-dockerhub-name/registry-demo:1.0.0
```

## Expected Output

- After build, `docker images` should show `registry-demo`
- After tagging, `docker images` should show the fully tagged name
- After push, the image should appear in your registry account if you are logged in

## What You Are Learning

- How to build a small image for sharing
- How to tag it correctly
- How to push it to a registry
