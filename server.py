from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from database.models import init_database, get_tasks

app = FastAPI()

# Initialise la base au démarrage
init_database()


# =========================
# API ENDPOINTS
# =========================

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
        }
    }


# =========================
# WEB UI (MOBILE FRIENDLY)
# =========================

@app.get("/ui", response_class=HTMLResponse)
def ui():

    tasks = get_tasks()

    tasks_html = ""

    for t in tasks:
        status = "✔" if t["completed"] else "⏳"

        tasks_html += f"""
        <div class="card">
            <h3>{status} {t['title']}</h3>
            <p>Date: {t['date']} | Heure: {t['time']}</p>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Herbert Life</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {{
                font-family: Arial;
                background: #0f172a;
                color: white;
                margin: 0;
                padding: 20px;
            }}

            h1 {{
                color: #38bdf8;
                text-align: center;
            }}

            .card {{
                background: #1e293b;
                padding: 15px;
                margin: 10px 0;
                border-radius: 10px;
            }}

            .stats {{
                background: #334155;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 20px;
            }}

            button {{
                padding: 10px;
                background: #38bdf8;
                border: none;
                border-radius: 8px;
                width: 100%;
                margin-top: 10px;
            }}
        </style>
    </head>

    <body>

        <h1>📊 Herbert Life</h1>

        <div class="stats">
            <p>Total tasks: {len(tasks)}</p>
            <p>Done: {len([t for t in tasks if t['completed']])}</p>
            <p>Pending: {len([t for t in tasks if not t['completed']])}</p>
        </div>

        <button onclick="location.reload()">🔄 Refresh</button>

        <h2>Tasks</h2>

        {tasks_html}

    </body>
    </html>
    """