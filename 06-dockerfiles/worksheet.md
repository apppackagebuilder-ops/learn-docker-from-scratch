# Worksheet: Dockerfiles, Build Context, and .dockerignore

## Part 1: Line by Line

Explain what each instruction does:

1. `FROM`
2. `WORKDIR`
3. `COPY`
4. `RUN`
5. `CMD`

## Part 2: Build Context

1. What does the final `.` mean in `docker build -t app .`?
2. Why can Docker usually copy only files inside the build context?
3. Why is running `docker build` from the correct folder important?

## Part 3: `.dockerignore`

1. Why is `.dockerignore` useful?
2. Name three things you might place in `.dockerignore`.

## Part 4: Practice

Build the Flask example and run it. Then explain:

- What happened during the build
- What happened when the container started
- Which step installs dependencies
