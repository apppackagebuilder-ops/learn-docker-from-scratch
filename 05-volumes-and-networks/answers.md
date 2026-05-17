# Answer Key: Volumes and Networks

## How to Use This Key

The most important lesson here is that storage and networking should be intentional, not guessed.

## Flow-1 Suggested Answers

1. Volumes help data survive container removal.
2. A bind mount uses a real host folder, while a named volume is managed by Docker.
3. `docker volume create app-data`

## Flow-2 Suggested Answers

1. Inside a container, `localhost` usually points back to that same container.
2. `docker network create app-net`
3. Names are easier and more stable than hard-coded IP addresses.

## Flow-3 Answers

1. `docker volume create app-data`
2. `docker network create app-net`
3. `docker run --rm -v app-data:/data alpine sh -c "cat /data/note.txt"`

## Flow-4 Reflection Guide

Important data should live in a volume or another persistent location so it survives container replacement.
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
