#  Unix-Inspired Task Manager API

A lightweight REST API inspired by Unix command-line tools (`ls`, `fork`, etc.) — built using **FastAPI** and **Python 3**. This task manager lets you create, view, update, and delete tasks, all stored in memory.

---

##  Features

-  Create a new task (`POST /tasks`)
-  List all tasks (`GET /tasks`)
-  View a single task by ID (`GET /tasks/{id}`)
-  Update task status (`PATCH /tasks/{id}?status=...`)
- Delete a task (`DELETE /tasks/{id}`)

---

##  Tech Stack

- **Python 3.8+**
- **FastAPI** – for building the API
- **Uvicorn** – ASGI server
- **Pydantic** – for data validation

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api

2. Install dependencies
 pip install -r requirements.txt

3. Running the App

Start the development server with:
uvicorn main:app --reload
Open your browser and visit:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
