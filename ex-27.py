"""ex-27.py"""

import requests, sys
from config import LINK_JSONPLACEHOLDER
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QFileDialog,
    QMessageBox,
)

class MainWindow(QMainWindow):
    """
    Controls the entire UI window
    """
    def __init__(self):
        """
        Initialises:
            self.url: str
            self.fetch: class

        Start:
            initUI: func
        """
        super().__init__()
        self.url = LINK_JSONPLACEHOLDER
        self.fetch = Fetch(self.url)

        self.initUI()

    def initUI(self) -> None:
        """
        Create the entire UI on the window

        Output:
            None
        """
        self.setWindowTitle("Site Request jsonplaceholder")
        self.setGeometry(100, 100, 500, 500)
        

        self.button = QPushButton(text="Select a Folder", parent=self)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.setGeometry(0, 0, 100, 50)

        self.fetch_button = QPushButton(text="Fetch", parent=self)
        self.fetch_button.clicked.connect(self.the_fetch_button_was_clicked)
        self.fetch_button.setGeometry(0, 60, 100, 50)

        self.save_button = QPushButton(text="Save Fetch", parent=self)
        self.save_button.clicked.connect(self.the_save_button_was_clicked)
        self.save_button.setGeometry(0, 120, 100, 50)

    def the_button_was_clicked(self) -> None:
        """
        Save a folder path when the button was clicked

        Output:
            None
        """
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select a Folder")
    
    def the_fetch_button_was_clicked(self) -> None:
        """
        Saves the fetch to self.got_fetch
        
        Output:
            self.got_fetch: str
        """
        self.got_fetch = self.fetch.get_fetch()
    
    def the_save_button_was_clicked(self) -> None:
        """
        Saves self.got_fetch to the selected folder

        Output:
            None
        """
        with open(self.folder_path + '/users.json', 'w') as file:
            file.write(self.got_fetch)


class Fetch:
    """
    Sends a request to the site via a link using the get_fetch function

    Args:
        url: str
    """
    def __init__(self, url: str) -> None:
        self.url = url
    
    def get_fetch(self) -> str:
        """
        Sends a request to the site via a link

        Output:
            response.text: str
        """
        response = requests.get(self.url)
        return response.text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
