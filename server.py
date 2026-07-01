from fastapi import FastAPI
from database.models import init_database, get_tasks

app = FastAPI()

init_database()


@app.get("/")
def home():
    return {
        "app": "Herbert Life",
        "status": "online",
        "version": "1.0"
    }


@app.get("/tasks")
def tasks():
    return {
        "count": len(get_tasks()),
        "tasks": get_tasks()
    }


@app.get("/dashboard")
def dashboard():

    tasks = get_tasks()

    total = len(tasks)
    done = len([t for t in tasks if t["completed"]])
    pending = total - done

    rate = round((done / total * 100), 2) if total > 0 else 0

    return {
        "stats": {
            "total": total,
            "done": done,
            "pending": pending,
            "completion_rate": rate
        },
        "tasks": tasks
    }