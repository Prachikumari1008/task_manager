#  Unix-Inspired Task Manager API

A lightweight REST API inspired by Unix command-line tools (`ls`, `fork`, etc.) — built using **FastAPI** and **Python 3**. This task manager lets you create, view, update, and delete tasks, all stored in memory.

---

## 🚀 Features

- 📝 Create a new task (`POST /tasks`)
- 📋 List all tasks (`GET /tasks`)
- 🔍 View a single task by ID (`GET /tasks/{id}`)
- ✏️ Update task status (`PATCH /tasks/{id}?status=...`)
- 🗑️ Delete a task (`DELETE /tasks/{id}`)

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
2. Create and activate a virtual environment
bash
Copy
Edit
# Create venv
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
 Running the App
Start the development server with:

bash
Copy
Edit
uvicorn main:app --reload
Open your browser and visit:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🧪 Example Usage (via Swagger UI or curl)
Create a task
bash
Copy
Edit
curl -X POST "http://127.0.0.1:8000/tasks" -H "Content-Type: application/json" -d '{"name": "Backup database"}'
Get all tasks
bash
Copy
Edit
curl http://127.0.0.1:8000/tasks
Update task status
bash
Copy
Edit
curl -X PATCH "http://127.0.0.1:8000/tasks/1?status=completed"
Delete a task
bash
Copy
Edit
curl -X DELETE "http://127.0.0.1:8000/tasks/1"
