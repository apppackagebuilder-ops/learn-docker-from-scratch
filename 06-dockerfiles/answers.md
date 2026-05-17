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
