from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.displayWidgets()

    def displayWidgets(self):
        self.setGeometry(100, 100, 400, 600)
        name_label = QLabel("Name:", self)
        name_label.move(50, 30)

        self.name_entry = QLineEdit(self)
        self.name_entry.resize(200, 20)
        self.name_entry.setAlignment(Qt.AlignLeft)
