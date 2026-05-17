# Answer Key: Installing Docker

## How to Use This Key

The important part is that you understand the checks and the order in which to run them.

## Flow-1 Suggested Answers

1. Docker Engine is the core software that runs containers, while Docker Desktop is the full application that packages the engine together with a UI and other tools.
2. Docker Desktop handles much of the setup work and gives beginners a simpler Windows experience.
3. `docker version`
4. `docker run hello-world`

## Flow-2 Answers

1. `docker version`
2. `docker info`
3. `docker run hello-world`
4. `docker ps -a`

## Flow-3 Suggested Answers

1. Reopen the terminal, restart Docker Desktop, or restart Windows if needed.
2. Wait for initialization, restart Docker Desktop, or check WSL integration.
3. Check whether Docker Desktop is running, whether the engine is responding, and what error message is shown.

## Flow-4 Reflection Guide

A good beginner answer explains this order:

1. Install Docker Desktop.
2. Start Docker Desktop and wait for it to be ready.
3. Run `docker version` and `docker info`.
4. Run `docker run hello-world` to confirm containers start correctly.
# Answer Key: Installing Docker

## Part 1 Suggested Answers

1. Docker Desktop is easier for beginners because it bundles Docker Engine, CLI tools, Compose, and Windows integration.
2. `docker version` shows client and server version information.
3. `docker info` shows detailed information about the Docker environment.
4. `docker run hello-world` proves Docker can download and run a container.

## Part 2

The checklist is complete when all commands run successfully and Docker Desktop is healthy.

## Part 3 Suggested Answers

If `docker` is not recognized:

- Reopen PowerShell
- Restart Docker Desktop
- Restart Windows if needed

If Docker Desktop is open but the engine is stopped:

- Wait for initialization or restart Docker Desktop
- Check WSL 2 or required Windows integration settings
