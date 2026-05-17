# Volume Demo

## Purpose

This example shows how data can survive across container runs when you use a volume.

## Build

```powershell
docker build -t volume-demo .
```

## Run

```powershell
docker run --rm -v practice-data:/data volume-demo
```

Run it more than once.

## Expected Output

Each run appends another line to the same file and prints the file contents.

That means:

- The container can disappear
- The data still remains in the volume

## What You Are Learning

- Why persistent storage matters
- How a named volume survives container removal
