# Answer Key: Images and Containers

## How to Use This Key

If the blueprint-versus-running-instance idea is clear, you are understanding the lesson correctly.

## Flow-1 Suggested Answers

1. An image is the packaged blueprint, while a container is the running or stopped instance created from it.
2. Because the image acts as a reusable template.
3. It downloads an image.
4. It creates and starts a container from an image.

## Flow-2 Answers

1. `docker pull nginx`
2. `docker run -d -p 8083:80 --name static-demo nginx`
3. `docker images`
4. `docker ps`

## Flow-3 Suggested Answers

1. `http://localhost:8083`
2. Nginx provides the web server.
3. The mounted HTML files provide the page content.

## Flow-4 Reflection Guide

The image is the prepared package. The container is what you get when that package is started.
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
