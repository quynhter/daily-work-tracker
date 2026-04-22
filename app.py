import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QScrollArea,
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton
)
from PySide6.QtCore import Qt

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
        header.setLayout(header_layout)
        central_layout.addWidget(header)
        
        body = QWidget()
        body_layout = QVBoxLayout()

        body_scroll = QScrollArea()
        body_scroll.setWidgetResizable(True)
        
        content = QWidget()
        content_layout = QVBoxLayout()
        content.setLayout(content_layout)

        for i in range(30):
            content_layout.addWidget(QPushButton(f"Кнопка {i}"))
        
        body_scroll.setWidget(content)
        body_layout.addWidget(body_scroll)

        body.setLayout(body_layout)
        central_layout.addWidget(body)

        footer = QWidget()
        footer_layout = QHBoxLayout()
        footer.setLayout(footer_layout)
        central_layout.addWidget(footer)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())