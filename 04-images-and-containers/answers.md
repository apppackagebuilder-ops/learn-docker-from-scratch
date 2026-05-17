# Answer Key: Images and Containers

## Part 1 Suggested Answers

1. An image is a packaged blueprint.
2. A container is an instance created from an image.
3. Yes. One image can create many containers.
4. `docker pull` downloads an image. `docker run` creates and starts a container from an image.

## Part 2 Suggested Answers

1. `docker pull` downloaded the Alpine image.
2. `docker run` created and started a container from that image.
3. Exiting the shell ended the main process, so the container stopped.

## Part 3 Suggested Answers

Two benefits of layers:

- Better build caching
- Faster rebuilds when only some steps change

## Part 4 Guidance

Commands like `docker images` show images. Commands like `docker ps` and `docker ps -a` show containers.
