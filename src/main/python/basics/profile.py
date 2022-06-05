from PyQt5.QtWidgets import QWidget

class ProfileWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("Profile")
        self.show()