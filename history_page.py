from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt


class HistoryPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.title = QLabel("📜 ประวัติ BMI")
        self.title.setAlignment(Qt.AlignCenter)

        self.history_label = QLabel("")
        self.history_label.setAlignment(Qt.AlignCenter)

        self.back_button = QPushButton("◀️ กลับ")

        layout.addWidget(self.title)
        layout.addWidget(self.history_label)
        layout.addWidget(self.back_button)

        self.setLayout(layout)