# Backend Software Challenge
For Habitat Energy  
Author: NoahMaze@ieee.org

# Scratch (delete later )
db creds
HOST db
PORT 5432
ENV POSTGRES_DB habitat
ENV POSTGRES_PASSWORD energy
USERNAME postgres
SCHEMA noah

## Usage
Run the demo: `docker compose up`

Docker will build the images, migrate the database, and kick off the work described in the challenge problem (hit the api, save the data, exit).

Verify that the data was saved by running these queries:
```SQL
# TBD
```

## Docker Images

### Postgres
The database container.
Automatically runs database migrations on first run.
The data is saved in the `noah` schema on the `habitat` database.
The schema migrations are generated automatically by alembic and saved to `db/migrations.sql`.

### App
Hits the API, saves the data, and exits.  
Data models are in `models.py`
API Integration is in `api.py`
The docker entrypoint is in `challenge.py`

## Docker Compose
Defines a `db` container and an `app` container, and shares the local directory with them.

## Python Modules

### api.py
Interacts with the Dynamic Containment API.  Returns JSON

### models.py
Describes the data model for the system

### challenge.py
Pulls data from the API and saves it to the database.
