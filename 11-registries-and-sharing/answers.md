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
