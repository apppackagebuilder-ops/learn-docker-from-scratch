# Environment and Startup Demo

## Purpose

This example shows how environment variables, `CMD`, and `ENTRYPOINT` affect container behavior.

## Build

```powershell
docker build -t env-demo .
```

## Run with Defaults

```powershell
docker run --rm env-demo
```

## Run with Custom Values

```powershell
docker run --rm -e APP_NAME=CourseApp env-demo --mode production
```

## Expected Output

You should see lines that print:

- The application name
- The application environment
- The selected mode

Those values change based on the environment variables and startup arguments you pass.
