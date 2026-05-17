# Worksheet: Environment Variables, CMD, and ENTRYPOINT

## Goal

Use this worksheet to confirm that you understand how runtime configuration changes container behavior.

## Before You Start

- Review the lesson and the `env-demo` example.
- Focus on defaults versus overrides.

## Flow-1: Concepts

1. What is an environment variable?
2. What is `CMD` used for?
3. What is `ENTRYPOINT` used for?
4. When are `CMD` and `ENTRYPOINT` often used together?

## Flow-2: Practice Commands

1. What command runs the `env-demo` image with default values?
2. What command runs it with `APP_NAME=CourseApp` and `--mode production`?
3. What part of the command changes the environment variable?
4. What part changes the startup argument?

## Flow-3: Example Check

1. Which value changes when you pass `-e APP_NAME=CourseApp`?
2. Which value changes when you pass `--mode production`?
3. Why can the same image behave differently without rebuilding?

## Flow-4: Reflection

Why is runtime configuration usually better than rebuilding the image for every small setting change?
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
