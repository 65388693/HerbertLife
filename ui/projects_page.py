from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton
)


class ProjectsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titre = QLabel("📂 Projets")
        titre.setStyleSheet("font-size:24px;font-weight:bold;")

        self.projects = QListWidget()

        self.btn_new = QPushButton("➕ Nouveau projet")

        layout.addWidget(titre)
        layout.addWidget(self.projects)
        layout.addWidget(self.btn_new)

        self.setLayout(layout)