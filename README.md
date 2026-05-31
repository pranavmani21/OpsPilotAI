# OpsPilotAI

## Backend

- Activate the virtual environment:
  - Windows Powershell: `.ackend\venv\Scripts\Activate.ps1`
  - Windows CMD: `.ackend\venv\Scripts\activate.bat`
- Install dependencies (if needed): `pip install -r backend\requirements.txt`
- Run the API:
  - `uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000`
- API endpoints:
  - `GET /api/hello`
  - `GET /api/status`

## Frontend

- Install Node.js and npm if not already installed.
- From `frontend` run:
  - `npm install`
  - `npm run dev`
- The Vite app will start on `http://localhost:5173`.

> The frontend dashboard page fetches backend status from `/api/status`.
