# Simple Web App

## Goal

This is the simplest final project in the course.

Its job is to help you feel comfortable with a full Docker mini-project without a lot of moving parts.

You will serve a static website using Nginx in Docker.

## What You Are Learning

This project helps you practice:

- Reading a Dockerfile
- Building an image
- Starting a project with Compose
- Opening the app in a browser
- Rebuilding after changing a file

## Project Files

### `Dockerfile`

This builds the image.
It starts from Nginx and copies the website files into the folder Nginx serves.

### `compose.yaml`

This starts the container for you with the port mapping already defined.

### `site/index.html`

This is the actual page content shown in the browser.

## Step-by-Step: Run It

Open a terminal in this project folder and run:

```powershell
docker compose up --build -d
```

What this does:

1. Reads `compose.yaml`
2. Builds the image from the Dockerfile
3. Starts the web container
4. Runs it in the background

## Open the App

Open this address in your browser:

`http://localhost:8088`

Expected result:

- You should see the sample web page from `site/index.html`

## What To Notice

- This project uses one container only
- Nginx serves static files
- Port `8088` on your machine maps to port `80` inside the container

## Stop It

When you are finished, run:

```powershell
docker compose down
```

## Beginner Practice Tasks

1. Change the text in `site/index.html`
2. Run `docker compose up --build -d` again
3. Refresh the browser
4. Explain why the page changed

## Questions To Ask Yourself

1. Which file describes how the image is built?
2. Which file describes how the container is started?
3. Why do you need `--build` after changing site content in this setup?
