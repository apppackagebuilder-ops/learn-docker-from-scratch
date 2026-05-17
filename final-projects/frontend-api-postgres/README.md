# Frontend, API, and PostgreSQL Project

## Goal

This project is a more realistic full-stack Docker example.

You will run three services together:

- `frontend`: a static web interface served by Nginx
- `api`: a Flask API
- `db`: a PostgreSQL database

## What You Learn

This project helps you practice:

- Running a frontend, backend, and database together
- Using Docker Compose for a multi-service app
- Reverse proxying API requests from the frontend
- Using a PostgreSQL volume for persistent data
- Reading how services connect to each other

## Read the Project Structure First

Look at these folders and files before you run anything:

- `frontend/`
- `api/`
- `database/`
- `compose.yaml`

## Step-by-Step: Start the Project

Open a terminal in this project folder and run:

```powershell
docker compose up --build -d
```

What this does:

1. Builds the frontend image
2. Builds the API image
3. Pulls the PostgreSQL image if needed
4. Creates the project network
5. Starts all three services

## Open the App

Open:

`http://localhost:8092`

Expected result:

- A small storefront page loads
- The page fetches product data from the API through the frontend Nginx proxy
- The API reads product rows from PostgreSQL

## Direct API Check

You can also open:

`http://localhost:8093/api/products`

Expected result:

- JSON containing seeded product data from the database

## Why the Data Exists Immediately

The project includes `database/init.sql`.

When PostgreSQL starts for the first time with an empty volume, it uses that file to create a table and insert sample rows.

## Why the Data Survives

The database uses a named volume called `storedata`.

That means the database files stay outside the short life of a single container.

## Stop the Project

```powershell
docker compose down
```

## Beginner Practice Tasks

1. Start the project
2. Open the frontend page
3. Open the direct API URL
4. Change one product row in `database/init.sql`
5. Recreate the project from scratch if you want to reseed the database
6. Change the page title in the frontend and rebuild
7. Explain how the browser reaches the API

## Questions To Ask Yourself

1. Which container serves the HTML page?
2. Which container talks to PostgreSQL?
3. Why does the browser only need the frontend port in normal use?
4. Which part of the project makes database data persistent?
