from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from ui.dashboard_page import DashboardPage
from ui.tasks_page import TasksPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Herbert Life")
        self.resize(1000, 600)

        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)

        self.pages = QStackedWidget()

        self.dashboard = DashboardPage()
        self.tasks = TasksPage()

        self.pages.addWidget(self.tasks)
        self.pages.addWidget(self.dashboard)

        self.btn_tasks = QPushButton("Tasks")
        self.btn_dashboard = QPushButton("Dashboard")

        self.btn_tasks.clicked.connect(lambda: self.pages.setCurrentWidget(self.tasks))
        self.btn_dashboard.clicked.connect(lambda: self.pages.setCurrentWidget(self.dashboard))

        self.layout.addWidget(self.btn_tasks)
        self.layout.addWidget(self.btn_dashboard)
        self.layout.addWidget(self.pages)