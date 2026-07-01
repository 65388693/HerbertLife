from database.models import get_tasks
from datetime import datetime, timedelta


def get_week_stats():

    tasks = get_tasks()
    today = datetime.now().date()

    total = 0
    done = 0
    streak = 0
    active_streak = True

    for i in range(7):

        day = today - timedelta(days=i)
        day_str = day.strftime("%Y-%m-%d")

        day_tasks = [t for t in tasks if t["date"] == day_str]

        if not day_tasks:
            active_streak = False
            continue

        day_done = [t for t in day_tasks if t["completed"]]

        total += len(day_tasks)
        done += len(day_done)

        if len(day_done) == len(day_tasks) and active_streak:
            streak += 1
        else:
            active_streak = False

    rate = round((done / total * 100), 2) if total > 0 else 0

    if rate >= 80:
        status = "🔥 Discipline forte"
    elif rate >= 50:
        status = "⚠️ Discipline moyenne"
    else:
        status = "❌ Procrastination détectée"

    return {
        "rate": rate,
        "streak": streak,
        "status": status
    }