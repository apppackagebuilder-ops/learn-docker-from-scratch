# Worksheet: Docker CLI Basics

## Goal

Use this worksheet to confirm that you can read, run, inspect, stop, and remove containers with the Docker CLI.

## Before You Start

- Review the CLI lesson.
- If possible, run the Nginx example while answering.

## Flow-1: Command Meaning

1. What does `docker ps` show?
2. What does `docker ps -a` show?
3. What does `docker logs` do?
4. What does `docker inspect` do?

## Flow-2: Write the Commands

Write the command to:

1. Run an Nginx container in detached mode on port `8080`.
2. List running containers.
3. Show logs for a container named `cli-nginx-demo`.
4. Stop a container named `cli-nginx-demo`.
5. Remove a container named `cli-nginx-demo`.

## Flow-3: Hands-On Check

1. Which browser URL should open the Nginx demo?
2. What command helps you confirm the container is still running?
3. What command helps you see low-level details about the container?

## Flow-4: Reflection

Why is it useful to inspect logs and container details instead of only starting containers?
# Worksheet: Docker CLI Basics

## Part 1: Command Meaning

Explain what each command does:

1. `docker ps`
2. `docker ps -a`
3. `docker images`
4. `docker logs my-container`
5. `docker exec -it my-container sh`

## Part 2: Break Down the Command

Explain each part of this command:

```powershell
docker run -d -p 8080:80 --name my-nginx nginx
```

## Part 3: Practice Flow

Put these actions in the correct order:

- View logs
- Stop container
- Start Nginx container
- Remove container
- Open site in browser

## Part 4: Reflection

1. Why is `--name` helpful?
2. Why is `-p` important for web apps?
3. What is one difference between `docker stop` and `docker rm`?
