# Final Projects

## Goal of This Section

Reading is useful, but building is what makes the ideas stick.

These final projects are here to help you move from:

- "I think I understand Docker"

to:

- "I can actually use Docker to build something real"

The projects move from simple to more realistic.

1. A static web app served by Nginx
2. PostgreSQL with pgAdmin using Compose
3. A small microservices demo
4. A frontend, API, and PostgreSQL full-stack project

## How to Use These Projects Properly

Do not just run them once and move on.

For each project, do this slowly:

1. Read the `README.md`
2. Inspect the Dockerfile or `compose.yaml`
3. Start the project yourself
4. Confirm it works
5. Change one thing
6. Rebuild or restart as needed
7. Explain to yourself what happened

That last step matters more than people think.

If you can explain:

- which container does what
- how they communicate
- where the data is stored

then you are really learning.

## Project List

1. [Simple Web App](../final-projects/simple-web-app/README.md)
2. [PostgreSQL and pgAdmin](../final-projects/postgres-pgadmin/README.md)
3. [Microservices Demo](../final-projects/microservices-demo/README.md)
4. [Frontend, API, and PostgreSQL](../final-projects/frontend-api-postgres/README.md)

## What Each Project Teaches

### Simple Web App

This teaches:

- A basic Dockerfile
- Port mapping
- Serving static files with Nginx

### PostgreSQL and pgAdmin

This teaches:

- Multi-container Compose setup
- Environment variables
- Persistent storage with a volume
- Service-to-service relationships

### Microservices Demo

This teaches:

- Multiple custom services
- Service naming and communication
- Building more than one image
- Thinking in small application pieces

### Frontend, API, and PostgreSQL

This teaches:

- A realistic three-service application
- Frontend to backend API flow
- Backend to database communication
- Persistent data with PostgreSQL
- Reverse proxy ideas with Nginx

## Final Challenge

After you run all three projects, build your own small application with:

- A frontend or API
- At least one database or supporting service
- A volume for persistent data
- A Compose file
- A short README explaining how to run it

## Graduation Checklist

By the time you can complete these projects confidently, you should be able to:

- Explain images, containers, volumes, and networks in plain language
- Build images with Dockerfiles
- Run multi-container apps with Compose
- Use environment variables and health checks
- Understand where data lives
- Apply practical beginner-friendly best practices

## Last Advice Before You Move On

If you still feel unsure, do not jump to Kubernetes or advanced orchestration yet.

Repeat these projects until the basics feel natural.

Strong Docker fundamentals matter much more than rushing into the next tool.
