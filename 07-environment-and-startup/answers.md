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
