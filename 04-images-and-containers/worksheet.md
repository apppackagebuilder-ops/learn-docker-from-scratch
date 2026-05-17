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
