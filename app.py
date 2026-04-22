import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QScrollArea,
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLineEdit
)
from PySide6.QtCore import Qt

def header_set(central_layout):
    edit = QLineEdit()
    edit.setPlaceholderText("Введите текст")
    central_layout.addWidget(edit)
    return central_layout

def content_set(content_layout):
    for i in range(30):
        content_layout.addWidget(QPushButton(f"Кнопка {i}"))
    return content_layout

def footer_set(footer_layout):
    edit = QLineEdit()
    edit.setPlaceholderText("Введите текст")
    footer_layout.addWidget(edit)
    return footer_layout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Реестр выполненных работ")
        self.resize(800, 600)
        
        central = QWidget()
        self.setCentralWidget(central)
        
        central_layout = QVBoxLayout()
        central_layout.setAlignment(Qt.AlignTop)
        central.setLayout(central_layout)
        
        header = QWidget()
        header_layout = QHBoxLayout()
        header_layout = header_set(header_layout)
        header.setLayout(header_layout)
        central_layout.addWidget(header)
        
        body = QWidget()
        body_layout = QVBoxLayout()

        body_scroll = QScrollArea()
        body_scroll.setWidgetResizable(True)
        
        content = QWidget()
        content_layout = QVBoxLayout()
        content_layout = content_set(content_layout)
        content.setLayout(content_layout)
        
        body_scroll.setWidget(content)
        body_layout.addWidget(body_scroll)

        body.setLayout(body_layout)
        central_layout.addWidget(body)

        footer = QWidget()
        footer_layout = QHBoxLayout()
        footer_layout = footer_set(footer_layout)
        footer.setLayout(footer_layout)
        central_layout.addWidget(footer)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())