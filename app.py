import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QAction, QScrollArea
)
from PyQt5.QtCore import Qt

class ArchitectApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Architect AI")
        self.setGeometry(100, 100, 800, 600)

        # Create menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # Add 'Close' action
        close_action = QAction("Close", self)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        main_layout = QVBoxLayout()

        # Chat box (scrollable)
        self.chat_box = QTextEdit()
        self.chat_box.setReadOnly(True)
        self.chat_box.setLineWrapMode(QTextEdit.WidgetWidth)

        # Scroll area for the chat box
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.chat_box)

        main_layout.addWidget(scroll_area)

        # Input box and prompt button
        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type your query here...")
        self.input_box.returnPressed.connect(self.handle_input)
        
        prompt_button = QPushButton("Prompt")
        prompt_button.clicked.connect(self.handle_input)

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(prompt_button)

        main_layout.addLayout(input_layout)

        # Set the central widget's layout
        central_widget.setLayout(main_layout)

    def handle_input(self):
        # Get text from the input box
        user_input = self.input_box.text()
        if user_input.strip():
            # Display the input in the chat box
            self.chat_box.append(f"You: {user_input}")
            # Clear the input box
            self.input_box.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ArchitectApp()
    main_window.show()
    sys.exit(app.exec_())
