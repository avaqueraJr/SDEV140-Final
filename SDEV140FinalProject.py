import sys
import webbrowser
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSizePolicy, QLabel, QVBoxLayout
from PyQt5.Qt import Qt

# Create the main window
class MyWidget(QWidget):
    # Initialize the main window
    def __init__(self):
        super().__init__()
        self.initUI()

    # Set up the user interface
    def initUI(self):
        # Set the window title and size
        self.setWindowTitle("Gamer's GUI")
        self.setGeometry(100, 100, 400, 300)

        # Create the description label and add it to the layout
        descriptionLabel = QLabel("Welcome to Gamer's GUI! Please choose a website ", self)
        descriptionLabel.setAlignment(Qt.AlignCenter)

        # Create the exit button and add it to the layout
        exitButton = QPushButton("Exit", self)
        exitButton.clicked.connect(QApplication.quit)
        exitButton.setShortcut("Ctrl+Q")

        # Create the YouTube button and label
        youtubeButton = QPushButton(self)
        youtubeButton.setIcon(QIcon("youtube.png"))
        youtubeButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        youtubeButton.clicked.connect(self.openYouTube)
        youtubeLabel = QLabel("YouTube", self)
        youtubeLabel.setAlignment(Qt.AlignCenter)

        # Create the Twitch button and label
        twitchButton = QPushButton(self)
        twitchButton.setIcon(QIcon("twitch.png"))
        twitchButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        twitchButton.clicked.connect(self.openTwitch)
        twitchLabel = QLabel("Twitch", self)
        twitchLabel.setAlignment(Qt.AlignCenter)

        # Create the TikTok button and label
        tiktokButton = QPushButton(self)
        tiktokButton.setIcon(QIcon("tiktok.png"))
        tiktokButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tiktokButton.clicked.connect(self.openTikTok)
        tiktokLabel = QLabel("TikTok", self)
        tiktokLabel.setAlignment(Qt.AlignCenter)

        # Create a vertical layout and add the widgets to it
        layout = QVBoxLayout(self)
        layout.addWidget(descriptionLabel)
        layout.addWidget(youtubeButton)
        layout.addWidget(youtubeLabel)
        layout.addWidget(twitchButton)
        layout.addWidget(twitchLabel)
        layout.addWidget(tiktokButton)
        layout.addWidget(tiktokLabel)
        layout.addWidget(exitButton)

    #Open website
    def openYouTube(self):
        webbrowser.open("https://www.youtube.com/")

    def openTwitch(self):
        webbrowser.open("https://www.twitch.tv/")

    def openTikTok(self):
        webbrowser.open("https://www.tiktok.com/")

app = QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
