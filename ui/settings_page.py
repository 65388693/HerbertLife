from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        titre = QLabel("⚙ Paramètres")
        titre.setStyleSheet("font-size:24px;font-weight:bold;")

        texte = QLabel(
            "Les paramètres seront ajoutés progressivement.\n\n"
            "- Notifications\n"
            "- Téléphone\n"
            "- Thème\n"
            "- Sauvegarde\n"
        )

        layout.addWidget(titre)
        layout.addWidget(texte)
        layout.addStretch()

        self.setLayout(layout)