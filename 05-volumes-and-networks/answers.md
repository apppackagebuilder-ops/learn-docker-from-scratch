# Answer Key: Volumes and Networks

## Part 1 Suggested Answers

1. Data written only inside a container can disappear because containers are easy to remove and recreate.
2. A named volume is persistent storage managed by Docker.
3. A bind mount connects a real folder from the host machine into the container.
4. A bind mount is often better for local development when you want to edit host files directly.

## Part 2 Suggested Answers

1. Networks let containers communicate with each other.
2. Inside a container, `localhost` usually points to that same container.
3. A custom network helps related containers find each other and stay organized.

## Part 3

The important proof is that the file survives when the second container reads it from the same volume, and one container can reach another by name on the shared network.
