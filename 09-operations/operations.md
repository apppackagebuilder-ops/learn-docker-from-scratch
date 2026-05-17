# Operations: Health Checks, Logging, Limits, Backup, Restore, Troubleshooting

## Goal of This Lesson

Up to now, you have learned how to build and run containers.

This lesson is about taking care of them after they start.

That means learning how to answer questions like:

- Is my app healthy?
- Where do I read the logs?
- How do I stop one container from using too much memory?
- How do I protect important data?
- What should I check when something breaks?

## Health Checks

One of the most important beginner lessons is this:

> A running container is not always a healthy container.

That sounds simple, but it matters a lot.

An app might be "running" while still being broken.

For example:

- The process started, but the app is frozen
- The app cannot reach the database
- The app returns errors on its health endpoint

That is why health checks exist.

## What a Health Check Does

A health check is a test Docker runs to see whether the container is actually responding the way it should.

It is like asking the app:

"Are you alive and working, or are you only pretending to be alive?"

### Example in a Dockerfile

```Dockerfile
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python healthcheck.py
```

In plain language, this says:

- Every 30 seconds, try the health check
- Wait up to 5 seconds each time
- If it fails several times, mark the container as unhealthy

### Example in Compose

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
  interval: 10s
  timeout: 3s
  retries: 3
```

This example checks an HTTP endpoint inside the container.

## Logging

Logs are the app's way of telling you what it is doing.

When something goes wrong, logs are often the first clue.

Containerized apps usually should write logs to:

- Standard output
- Standard error

Why?

Because Docker can collect those streams and show them with `docker logs`.

### See logs

```powershell
docker logs my-container
docker logs -f my-container
```

The `-f` follows new log lines as they appear.

## Resource Limits

Containers share the host machine's CPU and memory.

If you let every container use as much as it wants, one badly behaved app can affect others.

That is why resource limits matter.

### Example with `docker run`

```powershell
docker run -d --memory="256m" --cpus="1.0" nginx
```

This means:

- Limit memory to about 256 MB
- Limit CPU use to about 1 CPU

### Example in Compose

```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 256M
```

Note:

Some resource settings behave differently depending on the Docker environment and orchestration mode.

For a beginner, the important idea is this:

> Containers share resources, so limits help prevent one service from taking too much.

## Backup and Restore

If a container uses a volume for important data, you should know how to save and recover that data.

Think of it like backing up family photos.
If the data matters, you do not want only one copy.

### Volume backup idea

1. Attach the volume to a temporary helper container
2. Create an archive of the files
3. Store the archive safely

### Volume restore idea

1. Create or identify the target volume
2. Attach it to a helper container
3. Extract the backup archive into that volume

The example scripts in this lesson show one PowerShell-based way to do that.

## Troubleshooting Checklist

When a container fails, beginners often jump randomly from one guess to another.

A better approach is to use a simple checklist.

Check these in order:

1. Is the container running?
2. If not, why did it stop?
3. What do the logs say?
4. Is the correct port published?
5. Is the app listening on the correct interface?
6. Is the container healthy?
7. Are environment variables correct?
8. Can it reach required services such as a database?
9. Is the correct volume mounted?

## Common Problems and Fixes

### Problem: Container exits immediately

Possible reasons:

- The main process finished quickly
- The startup command is wrong
- The app crashed on startup

Helpful commands:

```powershell
docker ps -a
docker logs <container-name>
```

### Problem: App not reachable from the browser

Possible reasons:

- Port mapping is missing
- The app listens only on `127.0.0.1` inside the container
- Another process already uses the host port

Common fixes:

- Publish the port with `-p`
- Make the app listen on `0.0.0.0`
- Choose a different host port if needed

### Problem: App cannot reach the database

Possible reasons:

- Wrong hostname
- Wrong username or password
- Wrong environment variables
- Database not ready yet
- Services not on the same network

Common fixes:

- Use the Compose service name
- Inspect logs for both services
- Check network settings
- Add health or wait logic if needed

## Example in This Lesson

This lesson includes a small Flask app with:

- A `/health` endpoint
- Logging output
- A health check script

That gives you a safe place to practice reading logs and understanding health status.

## Mini Summary

Remember these operations habits:

1. Running does not always mean healthy.
2. Logs are often the first debugging tool.
3. Resource limits can protect the host and other containers.
4. Important data should be backed up.
5. Troubleshooting works better when you follow a checklist.

## Quick Quiz

1. Why is a running container not always healthy?
2. Where should containerized apps usually write logs?
3. Why set resource limits?
4. What are two common reasons an app may not be reachable from the browser?
5. What is one reason a service may fail to reach its database?

## Exercise

1. Build and run the health-check example.
2. Watch the logs.
3. Inspect the container health state.
4. Read the backup scripts and explain each step in plain words.
5. Write your own troubleshooting checklist using the lesson as a guide.

## What Comes Next

Continue to [Security, Multi-Stage Builds, and Image Optimization](../10-security-and-optimization/security-and-optimization.md).
