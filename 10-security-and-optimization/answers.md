# Answer Key: Security and Optimization

## How to Use This Key

The lesson is about building better habits for images that will live beyond local experiments.

## Flow-1 Suggested Answers

1. Secrets in images can be exposed when images are shared, stored, or inspected.
2. It reduces risk if the app is compromised.
3. Trusted base images reduce surprise and risk.

## Flow-2 Suggested Answers

1. A multi-stage build uses multiple `FROM` stages so the final image can contain only what is needed at runtime.
2. It is faster to pull and usually has less attack surface.
3. It keeps unnecessary files out of the build context.

## Flow-3 Suggested Answers

1. The build stage usually contains more tools and dependencies.
2. The final runtime stage becomes the shipped image.
3. `http://localhost:3000`

## Flow-4 Reflection Guide

A working image may still be too large, less secure than necessary, or harder to maintain in real environments.
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
