# Volume Demo

## Goal

This example shows how container data can survive when you use a named volume.

## Pre-requisites

- Docker Desktop running

## Flow

### Step-1: Build the example image

```powershell
docker build -t volume-demo .
```

### Step-2: Run the container with a named volume

```powershell
docker run --rm -v practice-data:/data volume-demo
```

### Step-3: Run it again

```powershell
docker run --rm -v practice-data:/data volume-demo
```

## Expected Output

Each run appends another line to the same file and prints the file contents.

That proves:

- The container can disappear
- The data can remain in the volume

## What You Are Learning

- Why persistent storage matters
- How a named volume survives container removal
