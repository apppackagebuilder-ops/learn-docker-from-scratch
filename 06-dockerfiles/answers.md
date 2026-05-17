# Answer Key: Dockerfiles

## How to Use This Key

If you understand what each instruction does and why the order matters, you are in good shape.

## Flow-1 Suggested Answers

1. A Dockerfile is a text file with instructions for building an image.
2. `FROM` sets the base image.
3. `COPY` copies files into the image.
4. `CMD` sets the default startup command.

## Flow-2 Suggested Answers

1. `docker build -t flask-demo .`
2. `docker run -d -p 5000:5000 --name flask-demo-app flask-demo`
3. It keeps unnecessary files out of the build context and helps builds stay smaller and cleaner.

## Flow-3 Suggested Answers

1. `requirements.txt`
2. `http://localhost:5000`
3. `docker logs flask-demo-app`

## Flow-4 Reflection Guide

A Dockerfile gives the team one repeatable build recipe instead of everyone setting up the app manually in different ways.
# Answer Key: Dockerfiles, Build Context, and .dockerignore

## Part 1 Suggested Answers

1. `FROM` chooses the base image.
2. `WORKDIR` sets the working directory inside the image.
3. `COPY` copies files into the image.
4. `RUN` executes a command during the image build.
5. `CMD` sets the default startup command.

## Part 2 Suggested Answers

1. The final `.` means use the current folder as the build context.
2. Docker receives that context as the set of files available during the build.
3. If you build from the wrong folder, needed files may not be available to `COPY`.

## Part 3 Suggested Answers

1. `.dockerignore` keeps unnecessary files out of the build context.
2. Common entries: `.git`, `node_modules`, `__pycache__`, `.env`.

## Part 4 Guidance

Dependency installation happens in the `RUN pip install ...` step. The container starts later using the `CMD` instruction.
