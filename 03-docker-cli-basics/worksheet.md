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
