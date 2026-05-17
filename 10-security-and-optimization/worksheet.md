# Worksheet: Security and Optimization

## Goal

Use this worksheet to confirm that you understand why a working image should also be smaller, safer, and cleaner.

## Before You Start

- Review the lesson and the multi-stage Node example.
- Focus on production-minded habits.

## Flow-1: Security Check

1. Why should you avoid putting secrets in images?
2. Why is running as a non-root user safer?
3. Why should you use trusted base images?

## Flow-2: Optimization Check

1. What is a multi-stage build?
2. Why is a smaller runtime image often better?
3. What is one benefit of `.dockerignore`?

## Flow-3: Example Check

1. Which stage usually contains more build tools?
2. Which stage becomes the final runtime image?
3. Which URL should open the example app?

## Flow-4: Reflection

Why is a working image not automatically a good image?
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
