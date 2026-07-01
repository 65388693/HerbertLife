import sys
from PySide6.QtWidgets import QApplication
from database.models import init_database
from ui.main_window import MainWindow
from reminder import ReminderEngine


def main():

    init_database()

    app = QApplication(sys.argv)

    reminder = ReminderEngine()
    reminder.start()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()