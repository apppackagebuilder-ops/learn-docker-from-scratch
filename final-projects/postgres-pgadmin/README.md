# PostgreSQL and pgAdmin

## Goal

This project teaches you how a real multi-container setup starts to feel.

You will run:

- PostgreSQL as the database
- pgAdmin as a browser-based database tool

## What You Learn

This project helps you practice:

- Running more than one container together
- Using Docker Compose
- Using environment variables
- Keeping database data in a volume
- Connecting one service to another

## Read the Compose File First

Before you run anything, open `compose.yaml` and notice:

- There is a `db` service
- There is a `pgadmin` service
- The database has a named volume
- Both services get configuration values from environment variables

## Step-by-Step: Start the Project

Open a terminal in this folder and run:

```powershell
docker compose up -d
```

What this does:

1. Pulls the PostgreSQL image if needed
2. Pulls the pgAdmin image if needed
3. Creates the project containers
4. Creates the project network
5. Starts both services

## Open the Tools

### PostgreSQL

The database listens on port `5432`.

### pgAdmin

Open:

`http://localhost:8089`

## Login Details

### pgAdmin login

- Email: `admin@example.com`
- Password: `admin123`

### PostgreSQL connection values inside the Compose project

- Host: `db`
- Port: `5432`
- Database: `appdb`
- Username: `appuser`
- Password: `apppass`

Important beginner note:

Use `db` as the hostname from pgAdmin because that is the Compose service name.

## Why the Data Survives Restarts

The database files are stored in a named volume called `pgdata`.

That means the data does not live only inside the short-lived container filesystem.

## Stop the Project

```powershell
docker compose down
```

That stops the containers.
The named volume remains unless you explicitly remove it.

## Beginner Practice Tasks

1. Start the project
2. Open pgAdmin
3. Register the PostgreSQL server using the values above
4. Create a table
5. Insert one row
6. Stop the project
7. Start it again
8. Confirm the data still exists

## Questions To Ask Yourself

1. Why is the hostname `db` instead of `localhost`?
2. Which part of the Compose file makes the data persistent?
3. Which service is the database and which service is the admin tool?
