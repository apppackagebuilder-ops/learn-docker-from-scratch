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
