from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
import random


class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(100, 100, 600, 800)
        _label = QLabel(self)
        _label.setText("I am a simple label")
        _label.move(10, 20)
        self._label = _label
        _button = QPushButton("Push me", self)
        _button.clicked.connect(self.onButtonClick)
        _button.move(100, 100)
        self.show()

    def onButtonClick(self):
        font_sizes = [10, 20, 30]
        self._label.setFont(QFont("Arial", random.choice(font_sizes)))
        self._label.setWordWrap(True)
