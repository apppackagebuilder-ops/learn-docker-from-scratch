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
