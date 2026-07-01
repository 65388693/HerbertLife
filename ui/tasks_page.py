from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QHBoxLayout,
    QInputDialog,
    QMessageBox,
    QDialog,
    QFormLayout,
    QDateEdit,
    QTimeEdit
)

from PySide6.QtCore import QDate, QTime

from models import add_task, get_tasks, delete_task, complete_task


class TasksPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # TITLE
        self.title = QLabel("✅ Mes tâches")
        self.title.setStyleSheet("font-size:24px;font-weight:bold;")

        # LIST
        self.list_tasks = QListWidget()

        # BUTTONS
        buttons = QHBoxLayout()

        self.btn_add = QPushButton("➕ Ajouter")
        self.btn_done = QPushButton("✅ Terminer")
        self.btn_delete = QPushButton("🗑 Supprimer")
        self.btn_refresh = QPushButton("🔄 Actualiser")

        buttons.addWidget(self.btn_add)
        buttons.addWidget(self.btn_done)
        buttons.addWidget(self.btn_delete)
        buttons.addWidget(self.btn_refresh)

        # LAYOUT
        layout.addWidget(self.title)
        layout.addLayout(buttons)
        layout.addWidget(self.list_tasks)

        self.setLayout(layout)

        # EVENTS
        self.btn_add.clicked.connect(self.add_task_ui)
        self.btn_done.clicked.connect(self.complete_task_ui)
        self.btn_delete.clicked.connect(self.delete_task_ui)
        self.btn_refresh.clicked.connect(self.load_tasks)

        self.load_tasks()

    # ================= LOAD =================
    def load_tasks(self):
        self.list_tasks.clear()

        tasks = get_tasks()

        for task in tasks:

            status = "✅" if task["completed"] else "⏳"

            text = f"{status} [{task['id']}] {task['title']} - {task['date']} {task['time']}"

            self.list_tasks.addItem(text)

    # ================= ADD TASK =================
    def add_task_ui(self):

        title, ok = QInputDialog.getText(self, "Tâche", "Titre:")
        if not ok or not title:
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Nouvelle tâche")

        form = QFormLayout(dialog)

        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDate(QDate.currentDate())

        time_edit = QTimeEdit()
        time_edit.setTime(QTime.currentTime())

        form.addRow("📅 Date :", date_edit)
        form.addRow("⏰ Heure :", time_edit)

        btn = QPushButton("Ajouter")
        form.addWidget(btn)

        def save():
            date = date_edit.date().toString("yyyy-MM-dd")
            time = time_edit.time().toString("HH:mm")

            add_task(title, "", date, time)

            dialog.accept()
            self.load_tasks()

        btn.clicked.connect(save)

        dialog.exec()

    # ================= COMPLETE TASK =================
    def complete_task_ui(self):

        selected = self.list_tasks.currentItem()

        if not selected:
            QMessageBox.warning(self, "Erreur", "Sélectionne une tâche")
            return

        text = selected.text()

        try:
            task_id = int(text.split("[")[1].split("]")[0])
        except:
            QMessageBox.warning(self, "Erreur", "ID introuvable")
            return

        complete_task(task_id)
        self.load_tasks()

    # ================= DELETE TASK =================
    def delete_task_ui(self):

        selected = self.list_tasks.currentItem()

        if not selected:
            QMessageBox.warning(self, "Erreur", "Sélectionne une tâche")
            return

        text = selected.text()

        try:
            task_id = int(text.split("[")[1].split("]")[0])
        except:
            QMessageBox.warning(self, "Erreur", "ID introuvable")
            return

        delete_task(task_id)
        self.load_tasks()