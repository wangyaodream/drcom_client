from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from PyQt6.QtCore import QTimer


class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        username_label = QLabel("username", self)
        self.username_input = QLineEdit(self)

        password_label = QLabel("password", self)
        password_input = QLineEdit(self)
        password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.show_info)

        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(password_input)
        layout.addWidget(self.start_button)

    def show_info(self):
        QMessageBox.information(self, "Hello!", self.username_input.text())


if __name__ == "__main__":
    app = QApplication([])

    window = SimpleApp()
    window.setWindowTitle("Demo")
    window.setFixedSize(300, 200)
    window.show()

    app.exec()
