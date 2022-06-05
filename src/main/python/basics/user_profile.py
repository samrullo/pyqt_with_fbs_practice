import profile
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont


class UserProfile(QWidget):
    def __init__(self, appctxt) -> None:
        super().__init__()
        self.appctxt = appctxt
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("User Profile")
        self.displayImages()
        self.displayUserInfo()

        self.show()

    def displayImages(self):
        background_image = self.appctxt.get_resource("images/blue_sky.png")
        profile_image = self.appctxt.get_resource("images/profile_image.png")

        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print(f"{background_image} image not found")

        try:
            with open(profile_image):
                profile = QLabel(self)
                pixmap = QPixmap(profile_image)
                profile.setPixmap(pixmap)
                profile.move(80, 20)
        except FileNotFoundError:
            print(f"{profile_image} is not found")

    def displayUserInfo(self):
        user_name = QLabel(self)
        user_name.setText("Sam Amrullo")
        user_name.move(85, 140)
        user_name.setFont(QFont("Arial", 20))

        bio_title = QLabel(self)
        bio_title.setText("Biography")
        bio_title.move(15, 170)
        bio_title.setFont(QFont("Arial", 17))

        about = QLabel(self)
        about.setText(
            "I am a software engineer with 10 years of expertise in python, Go and machine learning"
        )
        about.setWordWrap(True)
        about.move(15, 190)
