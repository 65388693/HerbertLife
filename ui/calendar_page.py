from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCalendarWidget


class CalendarPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titre = QLabel("📅 Calendrier")
        titre.setStyleSheet("font-size:24px;font-weight:bold;")

        calendrier = QCalendarWidget()

        layout.addWidget(titre)
        layout.addWidget(calendrier)

        self.setLayout(layout)