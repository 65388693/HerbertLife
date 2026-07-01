from database.models import get_tasks
from datetime import datetime


def get_today_stats():

    tasks = get_tasks()
    today = datetime.now().strftime("%Y-%m-%d")

    total = 0
    done = 0
    late = 0

    for t in tasks:

        if t["date"] != today:
            continue

        total += 1

        if t["completed"]:
            done += 1
        else:
            late += 1

    rate = round((done / total * 100), 2) if total > 0 else 0

    return {
        "total": total,
        "done": done,
        "late": late,
        "rate": rate
    }