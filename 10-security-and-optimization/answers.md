# Answer Key: Security and Optimization

## Part 1 Suggested Answers

1. Trusted base images reduce risk because you inherit from them.
2. Secrets in images can leak through shared layers, registries, and stored artifacts.
3. A non-root user reduces the damage possible if the app is compromised.

## Part 2 Suggested Answers

1. Smaller images are faster to pull and usually have less unnecessary software.
2. A multi-stage build keeps build tools out of the final runtime image.
3. `.dockerignore` keeps unnecessary files out of the build context.

## Part 3 Suggested Answers

1. The `deps` stage installs dependencies.
2. The `runtime` stage is the final runtime image.
3. The non-root user is created in the runtime stage.
