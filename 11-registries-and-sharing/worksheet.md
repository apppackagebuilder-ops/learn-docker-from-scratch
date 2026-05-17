# Worksheet: Registries and Sharing

## Goal

Use this worksheet to confirm that you understand how Docker images are shared through registries.

## Before You Start

- Review the registry lesson.
- Look at the tagging demo if you need a concrete example.

## Flow-1: Core Ideas

1. What is a Docker registry?
2. What is Docker Hub?
3. Why is tagging important?
4. Why can `latest` be risky?

## Flow-2: Commands

1. What command logs in to a registry?
2. What command tags `registry-demo` as `your-name/registry-demo:1.0.0`?
3. What command pushes that image?

## Flow-3: Practical Check

1. Why do you usually need to log in before pushing?
2. What two names should you see in `docker images` after tagging?
3. Why is a version tag clearer than only using `latest`?

## Flow-4: Reflection

Why do teams often prefer clear version tags over only using `latest`?
# Worksheet: Registries and Sharing

## Part 1: Basic Concepts

1. What is a Docker registry?
2. What is Docker Hub?
3. What does `docker push` do?
4. What does `docker pull` do?

## Part 2: Tagging

1. Why is tagging important before pushing an image?
2. Why can `latest` be risky?
3. Write an example tag using a username, image name, and version.

## Part 3: Practice

Use the tagging demo and write the commands you would use to:

1. Build the image
2. Tag the image
3. Push the image

## Part 4: Reflection

Why might a company prefer a private registry over a public one?
