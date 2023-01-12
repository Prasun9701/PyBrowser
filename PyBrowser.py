from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class webBrowser(QMainWindow):
    def __init__(self):
        super().__init__() # --> Inheriting the class methods from QMainWindow

        # Creating the main window and naming the application
        self.window = QWidget() # --> Creating an object of class QWidget
        self.window.setWindowTitle("PyBrowser")
        

        # Setting the vertical & horizontal layouts of the browser
        self.vertical_layout = QVBoxLayout()
        self.horizontal_layout = QHBoxLayout()

        # Button_1: Back Button
        self.back_button = QPushButton("⟵ Back") #--> The "⟵" argument (and similar ones below) sets the icon of the back button
        self.back_button.setMinimumHeight(30)
        self.back_button.clicked.connect(self.back_btn) # --> For click functionality
        
        # Button_2: Forward Button
        self.forward_button = QPushButton("Forward ⟶")
        self.forward_button.setMinimumHeight(30)
        self.forward_button.clicked.connect(self.forward_btn)

        # Button_3: Refresh Button
        self.refresh_button = QPushButton("Rel⟳ad")
        self.refresh_button.setMinimumHeight(30)
        self.refresh_button.clicked.connect(self.refresh_btn)
        
        # Button_4: Home Button
        self.home_button = QPushButton("🏠")
        self.home_button.setMinimumHeight(30)
        self.home_button.clicked.connect(self.home_btn)

        # Creating and managing the URL bar
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        # self.url_bar.returnPressed.connect(self)
        
        # Button_5: Search Button
        self.search_button = QPushButton("Search 🔍")
        self.search_button.setMinimumHeight(30)
        self.search_button.clicked.connect(self.navigate)
        self.search_button.setIcon(QIcon("C:\\Users\\Lenovo\\Desktop\\Python\\forward_button.png"))

        # Adding the buttons and the URL bar to the horizontal layout
        self.horizontal_layout.addWidget(self.back_button)
        self.horizontal_layout.addWidget(self.forward_button)
        self.horizontal_layout.addWidget(self.refresh_button)
        self.horizontal_layout.addWidget(self.home_button)
        self.horizontal_layout.addWidget(self.url_bar)
        self.horizontal_layout.addWidget(self.search_button)

        # Adding the web browsing functionality to the browser
        self.browser = QWebEngineView()

        # Adding the browser to the layout
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.vertical_layout.addWidget(self.browser)

        # Setting the home page
        self.url_bar.setText("https://google.com")
        self.browser.setUrl(QUrl("https://google.com")) # Instead of 'setUrl, 'load' can be used

        # Setting the layout
        self.window.setLayout(self.vertical_layout)
        self.window.show() # --> Displays the application window

    # Navigating the internet/ URL Bar Functionality
    def navigate(self, url):
        url = self.url_bar.toPlainText()
        if not url.startswith("https://"):
            url = "https://"+url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

    # Adding clickable functionalities to the buttons
    def back_btn(self):
        self.browser.back()
    def forward_btn(self):
        self.browser.forward()
    def refresh_btn(self):
        self.browser.reload()        
    def home_btn(self):
        self.browser.setUrl(QUrl("https://google.com"))

app = QApplication(sys.argv)
window = webBrowser()
app.exec_()