# Answer Key: Best Practices

## How to Use This Key

There may be more than one correct answer in this lesson because best practices often appear in several places.

## Flow-1 Suggested Answers

1. It keeps unnecessary files out of the build context.
2. They help detect containers that are running but not working properly.
3. They keep important data outside the disposable container filesystem.
4. It makes logs easier for Docker and other tools to collect.

## Flow-2 Suggested Answers

1. Example Dockerfile answer: dependency-first ordering, non-root user, or a clean base image.
2. Example Compose answer: easy startup, clear configuration, or readable service definitions.
3. Example application answer: health endpoint, configuration by environment variables, or stdout logging.

## Flow-3 Suggested Answers

1. It reduces risk if the app is compromised.
2. They help teams know exactly what they are running.
3. Documentation makes the project repeatable for other people.

## Flow-4 Reflection Guide

Best practices improve clarity, repeatability, safety, and maintainability, not just first-run success.
# Answer Key: Best Practices

## Part 1 Suggested Answers

1. `.dockerignore` keeps unnecessary files out of the build context.
2. Docker and other systems can collect those logs easily.
3. Fewer exposed ports reduce unnecessary access and confusion.
4. Documentation makes the setup easier for other people and for future maintenance.

## Part 2 Guidance

Possible good practices in `good-python-service` include:

- Clean `.dockerignore`
- Dependency-first build ordering
- Environment variables
- Health check
- Non-root user
- Compose-based startup

## Part 3

Answers depend on the project chosen, but they should reference real best practices from the lesson.
