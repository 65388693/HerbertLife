from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from analysis import get_today_stats
from coach_analysis import get_week_stats


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.label = QLabel()

        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.refresh()

    def refresh(self):

        s = get_today_stats()
        w = get_week_stats()

        self.label.setText(f"""
📊 TODAY

Total: {s['total']}
Done: {s['done']}
Late: {s['late']}
Rate: {s['rate']}%

----------------

🔥 WEEK

Streak: {w['streak']}
Rate: {w['rate']}%
Status: {w['status']}
""")