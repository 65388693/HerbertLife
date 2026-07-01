from fastapi import FastAPI
from database.models import init_database, get_tasks

app = FastAPI()

# init DB au démarrage
init_database()


@app.get("/")
def home():
    return {"status": "Herbert API Cloud OK"}


@app.get("/tasks")
def tasks():
    return get_tasks()


@app.get("/dashboard")
def dashboard():

    tasks = get_tasks()

    total = len(tasks)
    done = len([t for t in tasks if t["completed"]])
    late = len([t for t in tasks if not t["completed"]])

    rate = round((done / total * 100), 2) if total > 0 else 0

    return {
        "total": total,
        "done": done,
        "late": late,
        "rate": rate
    }