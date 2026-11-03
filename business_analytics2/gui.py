#!/usr/bin/env python3
'''
A simple GUI generated with Claude Opus 5.5; will add programming logic to offer this as an alternative to the CLI.
'''

import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit,
)


def process_input(text: str) -> str:
    """Replace this with your CLI program's logic.
    Take the user's input string and return the response string."""
    return f"You entered: {text}"


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Program")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Input:"))
        self.input_field = QLineEdit()
        self.input_field.returnPressed.connect(self.on_submit)  # Enter key also submits
        layout.addWidget(self.input_field)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.on_submit)
        layout.addWidget(self.submit_button)

        layout.addWidget(QLabel("Output:"))
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)
        layout.addWidget(self.output_field)

    def on_submit(self):
        user_text = self.input_field.text()
        response = process_input(user_text)
        self.output_field.setPlainText(response)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())