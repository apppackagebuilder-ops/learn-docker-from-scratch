# Hello World Demo

This example belongs to the introduction lesson.

Its job is very small on purpose.
It helps you see the simplest possible Docker flow:

1. Docker finds an image
2. Docker starts a container
3. The container prints a message
4. The container stops

## Run It

```powershell
./run-hello-world.ps1
```

If you prefer, you can run the raw command yourself:

```powershell
docker run hello-world
```

## Expected Output

You should see a success message from Docker explaining that the installation appears to be working correctly.

You should also see a stopped `hello-world` container if you run:

```powershell
docker ps -a
```

## What To Notice

- You did not build any code yet
- Docker can download an image for you
- A container can run only for a few seconds and still be useful
- A stopped container can still appear in `docker ps -a`
