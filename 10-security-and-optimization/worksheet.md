# Worksheet: Security and Optimization

## Part 1: Security Basics

1. Why should you use trusted base images?
2. Why should you avoid baking secrets into images?
3. Why is running as a non-root user safer?

## Part 2: Image Size

1. Why is a smaller image often better?
2. What is one benefit of a multi-stage build?
3. Why does `.dockerignore` help optimization?

## Part 3: Practice

Read the multi-stage Node example and answer:

1. Which stage installs dependencies?
2. Which stage becomes the runtime image?
3. Where is the non-root user created?

## Part 4: Reflection

Explain in plain words how a multi-stage build helps both image size and security.
