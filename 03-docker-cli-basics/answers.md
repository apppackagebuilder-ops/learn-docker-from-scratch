# Answer Key: Docker CLI Basics

## How to Use This Key

These commands matter because they form your basic container troubleshooting toolkit.

## Flow-1 Suggested Answers

1. `docker ps` shows running containers.
2. `docker ps -a` shows all containers, including stopped ones.
3. `docker logs` shows container output.
4. `docker inspect` shows detailed JSON metadata about a Docker object.

## Flow-2 Answers

1. `docker run -d -p 8080:80 --name cli-nginx-demo nginx`
2. `docker ps`
3. `docker logs cli-nginx-demo`
4. `docker stop cli-nginx-demo`
5. `docker rm cli-nginx-demo`

## Flow-3 Suggested Answers

1. `http://localhost:8080`
2. `docker ps`
3. `docker inspect cli-nginx-demo`

## Flow-4 Reflection Guide

Logs help you see what the application printed, and inspection helps you see configuration details like ports, environment, networks, and mounts.
# Answer Key: Docker CLI Basics

## Part 1 Suggested Answers

1. `docker ps` lists running containers.
2. `docker ps -a` lists all containers, including stopped ones.
3. `docker images` lists images on the machine.
4. `docker logs my-container` shows log output from that container.
5. `docker exec -it my-container sh` opens an interactive shell inside a running container.

## Part 2 Suggested Breakdown

- `docker run`: create and start a container
- `-d`: run in the background
- `-p 8080:80`: map host port 8080 to container port 80
- `--name my-nginx`: give the container a friendly name
- `nginx`: use the Nginx image

## Part 3 Correct Order

1. Start Nginx container
2. Open site in browser
3. View logs
4. Stop container
5. Remove container

## Part 4 Suggested Answers

1. It is easier than remembering a random ID.
2. Without port publishing, the browser may not reach the app.
3. `docker stop` stops a container, while `docker rm` removes a stopped container.
