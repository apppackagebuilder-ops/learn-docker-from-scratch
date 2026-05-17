# Answer Key: Registries and Sharing

## How to Use This Key

The main skill here is understanding image naming and knowing what you are actually sharing.

## Flow-1 Suggested Answers

1. A registry stores Docker images.
2. Docker Hub is a popular public Docker registry.
3. Tagging gives the image the full name and version used for sharing.
4. `latest` can be vague and may not clearly identify the exact deployed build.

## Flow-2 Suggested Answers

1. `docker login`
2. `docker tag registry-demo your-name/registry-demo:1.0.0`
3. `docker push your-name/registry-demo:1.0.0`

## Flow-3 Suggested Answers

1. Because registries usually require authentication before you upload images.
2. The local image name and the fully tagged registry name.
3. A version tag points to a specific build instead of a moving label.

## Flow-4 Reflection Guide

Teams need predictable, traceable deployments, and clear version tags make that much easier.
# Answer Key: Registries and Sharing

## Part 1 Suggested Answers

1. A registry stores Docker images.
2. Docker Hub is a common public registry for Docker images.
3. `docker push` uploads an image to a registry.
4. `docker pull` downloads an image from a registry.

## Part 2 Suggested Answers

1. Tagging gives the image the correct registry path and version name.
2. `latest` can be vague and make deployments harder to track.
3. Example: `myuser/myapp:1.0.0`

## Part 3 Guidance

A typical sequence is:

- `docker build -t registry-demo .`
- `docker tag registry-demo myuser/registry-demo:1.0.0`
- `docker push myuser/registry-demo:1.0.0`

## Part 4 Suggested Answer

A private registry gives an organization better access control, privacy, and internal governance.
