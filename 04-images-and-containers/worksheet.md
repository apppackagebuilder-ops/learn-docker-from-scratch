# Worksheet: Images and Containers

## Goal

Use this worksheet to make sure you clearly understand the difference between an image and a container.

## Before You Start

- Review the lesson and example first.
- Think about blueprint versus running object.

## Flow-1: Core Ideas

1. What is the difference between an image and a container?
2. Why can multiple containers be created from one image?
3. What does `docker pull` do?
4. What does `docker run` do?

## Flow-2: Write the Commands

1. Write the command to pull the Nginx image.
2. Write the command to run Nginx on host port `8083`.
3. Write the command to list images.
4. Write the command to list running containers.

## Flow-3: Example Check

1. What browser URL opens the static demo?
2. In that example, which part provides the web server?
3. Which part provides the page content?

## Flow-4: Reflection

Explain this sentence in your own words: `An image is the blueprint. A container is the running instance.`
# Worksheet: Images and Containers

## Part 1: Core Ideas

1. What is an image?
2. What is a container?
3. Can one image create more than one container?
4. What is the difference between `docker pull` and `docker run`?

## Part 2: Observe and Explain

Run:

```powershell
docker pull alpine
docker run -it alpine sh
```

Then answer:

1. What did `docker pull` do?
2. What did `docker run` do?
3. What happened when you exited the shell?

## Part 3: Layer Thinking

Why do Docker image layers help with builds?

Write two benefits.

## Part 4: Practice

1. Start an Nginx container.
2. View it with `docker ps`.
3. Stop it.
4. View it with `docker ps -a`.
5. Remove it.

Write which commands showed the image and which commands showed the container.
