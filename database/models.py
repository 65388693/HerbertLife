from database.database import get_connection


def init_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        date TEXT,
        time TEXT,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def get_tasks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()

    return [dict(row) for row in rows]


def add_task(title, date, time):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO tasks (title, date, time, completed)
    VALUES (?, ?, ?, 0)
    """, (title, date, time))

    conn.commit()
    conn.close()


def complete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    UPDATE tasks SET completed = 1 WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()