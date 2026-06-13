# OpsPilotAI

Sprint 0 foundation is in place:

- PostgreSQL runs via Docker Compose
- FastAPI connects to PostgreSQL
- SQLAlchemy is configured
- `tickets` table is created automatically on backend startup

## Current backend scope

Implemented today:

- FastAPI backend
- PostgreSQL 16 via Docker
- SQLAlchemy engine and ORM base
- First ORM model: `Ticket`
- Automatic table creation with `Base.metadata.create_all(...)`

Not implemented yet:

- Ticket create API
- AI services
- OpenAI integration
- Dashboard metrics
- Authentication

## Project structure

```text
backend/
  app/
    db/
      __init__.py
      database.py
    models/
      __init__.py
      ticket.py
  main.py
  requirements.txt
docker-compose.yml
frontend/
```

## PostgreSQL

Start the database:

```powershell
docker compose up -d db
```

Verify the container is running:

```powershell
docker ps
```

Current database container configuration:

- User: `postgres`
- Password: `password`
- Database: `opspilot`
- Port: `5432`

## Backend setup

Create or use the existing virtual environment, then install dependencies:

```powershell
backend\venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
```

Backend dependencies:

- `fastapi`
- `uvicorn`
- `sqlalchemy`
- `psycopg2-binary`

## Run the backend

From the `backend` directory:

```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Available endpoints:

- `GET /api/hello`
- `GET /api/status`

Backend status URL:

```text
http://127.0.0.1:8000/api/status
```

## Database connection

Database configuration currently defaults to:

```text
postgresql+psycopg2://postgres:password@localhost:5432/opspilot
```

Connection test:

```powershell
backend\venv\Scripts\python.exe backend\app\db\database.py
```

Expected result:

```text
Database Connected
```

## Ticket model

Current ORM model:

- table: `tickets`
- columns:
  - `id` integer primary key
  - `title` string
  - `description` text
  - `department` string
  - `priority` string

## Table creation

On backend startup, `backend/main.py` imports the `Ticket` model and runs:

```python
Base.metadata.create_all(bind=engine)
```

That creates the `tickets` table automatically if it does not already exist.

## Verify the tickets table

```powershell
docker compose exec -T db psql -U postgres -d opspilot -c "\dt"
```

Expected output includes:

```text
public | tickets | table | postgres
```

## Frontend

From `frontend`:

```powershell
npm install
npm run dev
```

The Vite frontend runs on:

```text
http://localhost:5173
```

The frontend dashboard currently reads backend status from `/api/status`.
