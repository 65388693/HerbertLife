import time
from database.models import get_tasks
from datetime import datetime


class ReminderEngine:

    def start(self):
        while True:
            self.check_tasks()
            time.sleep(60)

    def check_tasks(self):

        tasks = get_tasks()
        now = datetime.now()

        for t in tasks:

            if t["completed"]:
                continue

            try:
                task_time = datetime.strptime(
                    f"{t['date']} {t['time']}",
                    "%Y-%m-%d %H:%M"
                )

                if now > task_time:
                    print(f"⏰ Rappel: {t['title']}")

            except:
                pass