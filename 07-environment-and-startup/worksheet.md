# Worksheet: Environment Variables, CMD, and ENTRYPOINT

## Part 1: Core Ideas

1. What is an environment variable?
2. Why are environment variables useful in containers?
3. What does `CMD` do?
4. What does `ENTRYPOINT` do?

## Part 2: Compare

Write one sentence for each:

- Use `CMD` when...
- Use `ENTRYPOINT` when...
- Use both together when...

## Part 3: Practice

Build the `env-demo` example and run it:

1. With defaults
2. With a custom `APP_NAME`
3. With a different `--mode`

Then explain what changed each time.

## Part 4: Safety

Why is it better to pass configuration at runtime instead of hard-coding everything into the image?
