from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from PyQt6.QtCore import QThread

import drcom

class Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        drcom.main()

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        username_label = QLabel("username", self)
        self.username_input = QLineEdit(self)

        password_label = QLabel("password", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start)

        self.close_button = QPushButton("Close", self)
        self.close_button.clicked.connect(QApplication.instance().quit)

        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.close_button)

        self.work_thread = Worker()


    def start(self):
        drcom.username = self.username_input.text()
        drcom.password = self.password_input.text()
        self.work_thread.start()

    def get_username(self):
        return self.username_input.text()


if __name__ == "__main__":
    app = QApplication([])

    window = SimpleApp()
    window.setWindowTitle("Demo")
    window.setFixedSize(300, 200)
    window.show()

    app.exec()