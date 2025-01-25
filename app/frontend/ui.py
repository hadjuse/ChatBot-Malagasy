from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTextEdit
from PyQt6.QtCore import QPropertyAnimation, QRect, Qt
from PyQt6.QtGui import QFont
import sys

from pathlib import Path
import sys
project_root = Path(__file__).parents[2]
sys.path.append(str(project_root))
from app.backend.chatbot import *
class ChatbotUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Malagasy ChatBot")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f4f4f9;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.chat_layout = QVBoxLayout()
        self.input_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet(
            "background-color: #ffffff; border: 1px solid #ccc; border-radius: 8px; padding: 8px; font-size: 16px;"
        )
        self.main_layout.addWidget(self.chat_display)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.setStyleSheet(
            "border: 1px solid #ccc; border-radius: 8px; padding: 8px; font-size: 16px;"
        )

        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet(
            "background-color: #4CAF50; color: white; border: none; border-radius: 8px; padding: 10px 20px; font-size: 16px;"
        )
        self.send_button.setFont(QFont("Arial", 12))
        self.send_button.clicked.connect(self.send_message)

        self.input_layout.addWidget(self.input_field)
        self.input_layout.addWidget(self.send_button)
        self.main_layout.addLayout(self.input_layout)

        self.animation = QPropertyAnimation(self.input_field, b"geometry")
        self.animation.setDuration(300)
        self.animation.setStartValue(QRect(20, 500, 600, 30))
        self.animation.setEndValue(QRect(20, 500, 740, 30))
        self.animation.start()

    def send_message(self):
        user_message = self.input_field.text()
        if user_message.strip():
            self.chat_display.append(f"You: {user_message}")
            self.respond(user_message)
            self.input_field.clear()

    def respond(self, user_message):
        # Placeholder for chatbot response logic
        response = chatting(user_message, model)
        self.chat_display.append(f"Bot: {response}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot_ui = ChatbotUI()
    chatbot_ui.show()
    sys.exit(app.exec())
