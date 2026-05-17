# Worksheet: Dockerfiles

## Goal

Use this worksheet to confirm that you understand how a Dockerfile turns source code into a reusable image.

## Before You Start

- Review the Dockerfile lesson and the Flask example.
- Pay attention to instruction order.

## Flow-1: Core Dockerfile Ideas

1. What is a Dockerfile?
2. What does `FROM` do?
3. What does `COPY` do?
4. What does `CMD` do?

## Flow-2: Build Practice

1. What command builds an image and tags it as `flask-demo`?
2. What command runs that image on port `5000`?
3. Why is `.dockerignore` useful?

## Flow-3: Example Check

1. Which file installs Python dependencies in the example?
2. Which URL should you open after starting the container?
3. What command helps you see whether the app started correctly?

## Flow-4: Reflection

Why is a Dockerfile useful for teams and repeatable builds?
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
