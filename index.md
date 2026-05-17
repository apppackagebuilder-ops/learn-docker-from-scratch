# Docker Course Index

Welcome to the Docker course. This course starts from the absolute basics and gradually moves toward advanced, real-world Docker usage.

It is written for beginners, so the lessons intentionally explain ideas slowly before moving to commands.

## How to Study

- Read lessons in order.
- Do not rush. Understanding is more important than finishing quickly.
- Run the commands yourself.
- Type the files by hand when possible. You learn more that way.
- Do the exercises before looking at the final projects.
- Use each lesson's `worksheet.md` before opening `answers.md`.

## Learning Pattern Used in This Course

Most lessons follow a practical pattern:

1. Understand the idea in simple language
2. Review any pre-requisites
3. Follow numbered steps in order
4. Compare with sample or expected output
5. Practice with the example files
6. Review with the worksheet and answer key

## Beginner Learning Flows

If you want to study this repository like a training path instead of only a table of contents, use these flows.

### Flow-1: First Contact with Docker

1. [Introduction to Docker](./01-introduction/introduction.md)
2. [Installing Docker](./02-installation/installation.md)
3. [Docker CLI Basics](./03-docker-cli-basics/docker-cli-basics.md)

Quick practice links:

- [Hello world intro demo](./01-introduction/examples/hello-world-demo/README.md)
- [Installation verification example](./02-installation/examples/verification/README.md)
- [CLI Nginx demo](./03-docker-cli-basics/examples/nginx-cli-demo/README.md)

### Flow-2: Build and Run Containers

1. [Images and Containers](./04-images-and-containers/images-and-containers.md)
2. [Dockerfiles, Build Context, and .dockerignore](./06-dockerfiles/dockerfiles.md)
3. [Environment Variables, CMD, and ENTRYPOINT](./07-environment-and-startup/environment-and-startup.md)

Quick practice links:

- [Static image and container example](./04-images-and-containers/examples/README.md)
- [Flask Dockerfile example](./06-dockerfiles/examples/python-flask-app/README.md)
- [Environment and startup example](./07-environment-and-startup/examples/env-demo/README.md)

### Flow-3: Data and Multi-Container Applications

1. [Volumes and Networks](./05-volumes-and-networks/volumes-and-networks.md)
2. [Docker Compose and Multi-Container Apps](./08-docker-compose/docker-compose.md)
3. [Final Projects](./13-final-projects/final-projects.md)

Quick practice links:

- [Volume demo](./05-volumes-and-networks/examples/volume-demo/README.md)
- [Network demo](./05-volumes-and-networks/examples/network-demo/README.md)
- [Web and database Compose example](./08-docker-compose/examples/web-db-compose/README.md)
- [Final projects hub](./13-final-projects/final-projects.md)

### Flow-4: Operate and Improve What You Built

1. [Operations: Health Checks, Logging, Limits, Backup, Restore, Troubleshooting](./09-operations/operations.md)
2. [Security, Multi-Stage Builds, and Image Optimization](./10-security-and-optimization/security-and-optimization.md)
3. [Docker Hub and Private Registries](./11-registries-and-sharing/registries-and-sharing.md)
4. [Best Practices](./12-best-practices/best-practices.md)

Quick practice links:

- [Health check demo](./09-operations/examples/healthcheck-demo/README.md)
- [Backup demo](./09-operations/examples/backup-demo/README.md)
- [Multi-stage Node example](./10-security-and-optimization/examples/multi-stage-node/README.md)
- [Registry tagging demo](./11-registries-and-sharing/examples/tagging-demo/README.md)
- [Best practices service example](./12-best-practices/examples/good-python-service/README.md)

## Final Project Quick Start

If you want to jump directly into hands-on projects after the lessons, start here:

1. [Simple Web App](./final-projects/simple-web-app/README.md)
2. [PostgreSQL and pgAdmin](./final-projects/postgres-pgadmin/README.md)
3. [Microservices Demo](./final-projects/microservices-demo/README.md)
4. [Frontend, API, and PostgreSQL](./final-projects/frontend-api-postgres/README.md)

## Table of Contents

1. [Introduction to Docker](./01-introduction/introduction.md)
2. [Installing Docker](./02-installation/installation.md)
3. [Docker CLI Basics](./03-docker-cli-basics/docker-cli-basics.md)
4. [Images and Containers](./04-images-and-containers/images-and-containers.md)
5. [Volumes and Networks](./05-volumes-and-networks/volumes-and-networks.md)
6. [Dockerfiles, Build Context, and .dockerignore](./06-dockerfiles/dockerfiles.md)
7. [Environment Variables, CMD, and ENTRYPOINT](./07-environment-and-startup/environment-and-startup.md)
8. [Docker Compose and Multi-Container Apps](./08-docker-compose/docker-compose.md)
9. [Operations: Health Checks, Logging, Limits, Backup, Restore, Troubleshooting](./09-operations/operations.md)
10. [Security, Multi-Stage Builds, and Image Optimization](./10-security-and-optimization/security-and-optimization.md)
11. [Docker Hub and Private Registries](./11-registries-and-sharing/registries-and-sharing.md)
12. [Best Practices](./12-best-practices/best-practices.md)
13. [Final Projects](./13-final-projects/final-projects.md)

## Suggested Pace

- Beginner pace: one lesson per day
- Fast pace: two to three lessons per day
- Practice rule: for every 20 minutes of reading, spend 20 minutes typing and running commands

## Final Goal

By the end of this repository, you should be able to:

- Build your own Docker images
- Run and inspect containers
- Store data safely with volumes
- Connect containers with networks
- Use Compose for multi-container systems
- Debug common Docker issues
- Apply production-minded best practices
