# Installing Docker

## Goal

By the end of this lesson, you should be able to do three simple but important things:

1. Install Docker on Windows
2. Confirm that Docker is actually running
3. Run a tiny test container successfully

That may sound small, but it is a big milestone.
Once Docker is installed correctly, the rest of the course becomes much easier.

## Pre-requisites

- Windows 10 or Windows 11
- Administrator access
- Internet access

## Beginner Path in This Lesson

If you want the simplest possible route, do these in order:

1. Install Docker Desktop.
2. Wait until Docker Desktop says Docker is running.
3. Run `docker version` and `docker info`.
4. Run `docker run hello-world`.
5. If something fails, use the troubleshooting section at the end of this lesson.

## Flow-1: Install Docker and Verify It

### Step-1: Download Docker Desktop

Download Docker Desktop for Windows from the official Docker website.

### Step-2: Run the installer

Follow the install steps and enable WSL 2 integration if required.

### Step-3: Start Docker Desktop

Wait until Docker Desktop says Docker is running.

### Step-4: Verify Docker in PowerShell

```powershell
docker version
docker info
```

### Step-5: Run the first test container

```powershell
docker run hello-world
```

## Sample Output

The `hello-world` container should print a success message that confirms your Docker installation is working correctly.

Example output:

```text
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

## Visual Map

```mermaid
flowchart LR
	A[Install Docker Desktop] --> B[Start Docker Desktop]
	B --> C[Run docker version and docker info]
	C --> D[Run hello-world container]
	D --> E[Docker is ready for lessons]
```

## Installation Requirements

You do not need to be an expert.
You only need a machine that can run Docker Desktop comfortably.

Basic requirements:

- Windows 10 or Windows 11
- Administrator rights on the computer
- Internet access for downloading Docker and images
- Enough free disk space

## Docker Desktop vs Docker Engine

This is a place where beginners often get confused, so let us separate the words clearly.

### Docker Engine

Docker Engine is the core software that builds and runs containers.

### Docker Desktop

Docker Desktop is a Windows and Mac application that packages Docker Engine together with useful tools and a user-friendly interface.

On Windows, most beginners should use Docker Desktop.

Docker Desktop usually includes:

- Docker Engine
- Docker CLI
- Docker Compose
- Desktop settings and UI
- WSL 2 integration

## Why Windows Beginners Usually Use Docker Desktop

Because it handles a lot of setup work for you.

Instead of manually wiring together low-level pieces, Docker Desktop gives you a more complete experience.

For learning, this is the right tradeoff.

## How to Know Docker Is Ready

You can usually tell in two ways:

- Docker Desktop says it is running
- Terminal commands like `docker version` work without server errors

### What `docker version` tells you

It shows version information for:

- The Docker client
- The Docker server or engine

If the client shows up but the server does not, Docker may be installed but not fully running.

### What `docker info` tells you

It shows more detailed information such as:

- CPU and memory details
- Docker root directory
- Storage details
- Number of images and containers

Do not worry if much of this output looks unfamiliar.
At this stage, you only need to confirm that Docker responds successfully.

## What Happens During `hello-world`

When you run `docker run hello-world`, Docker:

1. Checks whether the image already exists on your machine.
2. Downloads it if it is missing.
3. Starts a container from that image.
4. Prints a success message.
5. Stops the container because the task is finished.

## Useful First Checks

After running `hello-world`, try these:

### List images

```powershell
docker images
```

You should see the `hello-world` image listed.

### List containers

```powershell
docker ps -a
```

You should see the `hello-world` container, even though it is stopped.

That teaches an important lesson already:

Stopped containers still exist until you remove them.

## Sample Code for This Lesson

This lesson includes a verification script in `examples/verification/check-docker-installation.ps1`.

That script runs the same beginner checks from this lesson in one place:

- `docker version`
- `docker info`
- `docker run hello-world`
- `docker images`
- `docker ps -a`

Use it after installation if you want a quick confidence check.

## If Docker Does Not Start

Do not panic.
Installation issues are common and usually fixable.

Try these checks in order:

1. Make sure Docker Desktop is open
2. Wait a little longer for the engine to initialize
3. Restart Docker Desktop
4. Restart the computer
5. Confirm WSL 2 is enabled if Docker expects it
6. Confirm virtualization is enabled if your machine requires it

## Common Installation Problems

### Problem: `docker` command is not recognized

Possible reasons:

- Docker Desktop did not install correctly
- The terminal was open before installation finished
- Environment variables or PATH were not refreshed yet

Try this:

- Close and reopen PowerShell
- Restart Docker Desktop
- Restart Windows if needed

### Problem: Docker Desktop opens, but the engine is stopped

Possible reasons:

- Docker is still initializing
- WSL integration is misconfigured
- A required Windows feature is missing

Try this:

- Wait briefly and retry
- Restart Docker Desktop
- Check Docker Desktop settings for WSL integration

### Problem: Virtualization or permission errors

Possible reasons:

- Virtualization is disabled in BIOS or UEFI
- Required Windows features are missing
- Installation was not done with the needed permissions

Try this:

- Run the installer with admin rights
- Enable virtualization if required
- Enable the Windows features Docker Desktop asks for

## Beginner Tip

Right now, your goal is not to understand every system detail.

Your goal is simply:

- Docker is installed
- Docker is running
- Docker can run a container

That is enough to move forward.

## Mini Summary

Remember these four points:

1. On Windows, beginners usually install Docker Desktop.
2. Docker Desktop includes Docker Engine and other helpful tools.
3. `docker version` and `docker info` help verify the setup.
4. `docker run hello-world` is the first real proof that Docker works.

## Practice Commands

Run these commands and say out loud what each one is checking:

```powershell
docker version
docker info
docker run hello-world
docker images
docker ps -a
```

## Quick Quiz

1. Why do most Windows beginners use Docker Desktop instead of manually installing only Docker Engine?
2. What does `docker run hello-world` prove?
3. What does `docker ps -a` show that `docker ps` does not?

## Exercise

Complete this checklist:

- Docker Desktop installed
- Docker Desktop running
- `docker version` works
- `docker info` works
- `docker run hello-world` works
- `docker images` shows `hello-world`
- `docker ps -a` shows the test container

## What Comes Next

Continue to [Docker CLI Basics](../03-docker-cli-basics/docker-cli-basics.md).
