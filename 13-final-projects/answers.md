# Answer Key: Final Projects

## How to Use This Key

Some answers vary depending on which project you choose. The important part is whether you can explain the project clearly.

## Flow-1 Suggested Answers

1. The simplest starting point is the Simple Web App project.
2. The PostgreSQL and pgAdmin project includes PostgreSQL and pgAdmin.
3. The Microservices Demo demonstrates service-to-service communication.
4. The Frontend, API, and PostgreSQL project includes a frontend, API, and database together.

## Flow-2 Suggested Answers

A good answer should identify:

1. The services or containers in the chosen project.
2. The exposed host ports.
3. Whether data is stored in a named volume or not stored persistently.
4. The startup file, usually `compose.yaml`.

## Flow-3 Suggested Answers

1. In browser-facing projects, the frontend or gateway service talks to the browser first.
2. The database service stores data when a database exists.
3. Services usually find each other by service name on the Docker network.

## Flow-4 Reflection Guide

Changing and rebuilding teaches you how Docker responds to edits, rebuilds, networking, and data persistence in a real project.
# Answer Key: Final Projects

## Part 1 Guidance

Learners should compare each project by containers, Compose usage, storage needs, and learning focus.

## Part 2 Sample Ideas

1. The simple web app is usually easiest because it has only one service.
2. PostgreSQL plus pgAdmin often feels more realistic because it includes a real database and admin tool.
3. The microservices demo best demonstrates service-to-service communication.

## Part 3 Guidance

A good answer names a small app, lists its services clearly, identifies persistent data, and includes environment variables and a volume where appropriate.

## Part 4 Guidance

A good reflection should describe understanding of images, containers, networking, storage, Dockerfiles, and Compose in the learner's own words.
