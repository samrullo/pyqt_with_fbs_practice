from PyQt5.QtWidgets import (
    QWidget,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)
from PyQt5.QtGui import QFont


class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Special big button")
        _label = QLabel("Special Button", self)
        _label.setStyleSheet(
            """background-color:darkblue;
        color:white;
        border-style:outset;
        border-width:3px;
        border-radius: 5px;
        font: 30px 'Arial';
        qproperty-alignment: AlignCenter"""
        )
        _line_edit = QLineEdit(self)
        _line_edit.setStyleSheet("""color:red;font: bold 30px 'Arial';""")
        _btn = QPushButton("I am special", self)
        _btn.setObjectName("special_button")
        _btn_two = QPushButton("I am special too", self)
        _btn_two.setObjectName("special_button")
        _vbox = QVBoxLayout()
        _vbox.addWidget(_label)
        _vbox.addWidget(_line_edit)
        _vbox.addWidget(_btn)
        _vbox.addWidget(_btn_two)
        self.setLayout(_vbox)
        self.show()
