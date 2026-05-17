# Answer Key: Environment Variables, CMD, and ENTRYPOINT

## How to Use This Key

The key idea is understanding which part of container behavior is fixed and which part is configurable.

## Flow-1 Suggested Answers

1. An environment variable is a named value given to a program at runtime.
2. `CMD` sets the default command or default arguments.
3. `ENTRYPOINT` sets the main executable.
4. They are often used together when the executable stays the same but the default arguments may change.

## Flow-2 Suggested Answers

1. `docker run --rm env-demo`
2. `docker run --rm -e APP_NAME=CourseApp env-demo --mode production`
3. `-e APP_NAME=CourseApp`
4. `--mode production`

## Flow-3 Suggested Answers

1. The application name value changes.
2. The mode value changes.
3. Because configuration is passed at runtime instead of being hard-coded into a new image build.

## Flow-4 Reflection Guide

Runtime configuration keeps the image reusable across development, testing, and production without needing a rebuild for every small value change.
# Answer Key: Environment Variables, CMD, and ENTRYPOINT

## Part 1 Suggested Answers

1. An environment variable is a named value given to a program at runtime.
2. It lets the same image behave differently in different environments.
3. `CMD` provides a default command or default arguments.
4. `ENTRYPOINT` defines the main executable for the container.

## Part 2 Suggested Answers

- Use `CMD` when you want a default command that can be replaced easily.
- Use `ENTRYPOINT` when the container should always run one main executable.
- Use both together when the program stays fixed but default arguments should be changeable.

## Part 3 Guidance

Changing `APP_NAME` changes the environment-based output. Changing `--mode` changes the startup argument output.

## Part 4 Suggested Answer

Runtime configuration is better because the same image can be reused without rebuilding for every environment.
