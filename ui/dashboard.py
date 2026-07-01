from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from analysis import get_today_stats
from coach_analysis import get_week_stats


class Dashboard(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()

        self.title = QLabel("📊 Dashboard Discipline")
        self.title.setStyleSheet("font-size:26px;font-weight:bold;")

        self.stats_label = QLabel()
        self.stats_label.setStyleSheet("font-size:16px;")

        self.refresh_btn = QPushButton("🔄 Actualiser")

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.stats_label)
        self.layout.addWidget(self.refresh_btn)

        self.setLayout(self.layout)

        self.refresh_btn.clicked.connect(self.refresh)

        self.refresh()

    def refresh(self):

        stats = get_today_stats()
        week = get_week_stats()

        text = f"""
📅 AUJOURD'HUI

✔ Total tâches : {stats['total']}
✅ Terminées : {stats['done']}
⏰ En retard : {stats['late']}
📊 Discipline jour : {stats['rate']} %

────────────────────

📆 SEMAINE

🔥 Streak : {week['streak']} jours
📊 Score semaine : {week['rate']} %
🧠 Analyse : {week['status']}
"""

        self.stats_label.setText(text)