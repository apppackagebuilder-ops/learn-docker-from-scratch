# Worksheet: Docker Compose and Multi-Container Apps

## Part 1: Understanding Compose

1. What problem does Docker Compose solve?
2. What is a `compose.yaml` file used for?
3. What does `docker compose up -d` do?
4. What does `docker compose down` do?

## Part 2: Service Communication

1. Why can one service usually reach another by service name?
2. Why is `localhost` often wrong inside a container?
3. What is the role of `depends_on`?

## Part 3: Practice

Run the `web-db-compose` example and answer:

1. Which service is the web app?
2. Which service is the database?
3. What port do you open in the browser?
4. What hostname does the app use to reach PostgreSQL?

## Part 4: Reflection

Explain how Compose makes a two-container app easier than writing long manual `docker run` commands.
