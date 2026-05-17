# Answer Key: Operations

## How to Use This Key

The goal here is to build good operating habits, not just memorize commands.

## Flow-1 Suggested Answers

1. A process can be running even when the application is not responding correctly.
2. A health check tests whether the app is responding as expected.
3. `docker logs <container-name>`
4. `docker logs -f <container-name>`

## Flow-2 Suggested Answers

1. Limits help prevent one container from using too many host resources.
2. Backup matters because volume data may be important and should be recoverable.
3. Check `docker ps -a` and `docker logs <container-name>`.

## Flow-3 Suggested Answers

1. `http://localhost:5002/health`
2. `docker inspect healthcheck-demo`
3. `volume-backup.tar`

## Flow-4 Reflection Guide

A checklist keeps troubleshooting focused and repeatable, while random guessing wastes time and often misses the real cause.
# Answer Key: Operations

## Part 1 Suggested Answers

1. The main process may be running even if the app is frozen or returning errors.
2. A health check tests whether the app is actually responding correctly.
3. Docker can collect those log streams and show them with `docker logs`.

## Part 2 Suggested Answers

1. Limits prevent one container from using too much CPU or memory.
2. Important data should be recoverable if something goes wrong.
3. Attach the volume to a temporary container, archive the files, and save the archive.

## Part 3 Suggested Answers

Web app checks may include:

- Is the container running?
- Is the port published?
- Is the app listening on `0.0.0.0`?
- What do the logs show?

Possible reasons a container exits immediately:

- The main process finished
- The startup command is wrong
- The app crashed
