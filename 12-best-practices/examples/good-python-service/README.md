# Good Python Service Example

This example bundles several best practices into one small project.

## What It Demonstrates

- A small trusted base image
- Dependency installation before copying the full app
- `.dockerignore` to keep the build context clean
- Environment variables for configuration
- Logging to standard output
- A health check endpoint
- Running as a non-root user
- A Compose file for easy local startup

## Run It

```powershell
docker compose up --build -d
```

Open `http://localhost:8010`

## Expected Output

You should see a JSON response that includes the service name, environment, and a short message.

If you open:

`http://localhost:8010/health`

you should see a simple healthy response.

## Health Check

The service also exposes:

`http://localhost:8010/health`

## Stop It

```powershell
docker compose down
```
