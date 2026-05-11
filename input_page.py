# =========================
# input_page.py
# =========================

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)


class InputPage(QWidget):
    def __init__(self):
        super().__init__()

        # ===== Layout =====
        layout = QVBoxLayout()

        # ===== น้ำหนัก =====
        weight_label = QLabel("น้ำหนัก (กิโลกรัม)")

        self.weight_input = QLineEdit()

        self.weight_input.setPlaceholderText(
            "กรอกน้ำหนัก"
        )

        # ===== ส่วนสูง =====
        height_label = QLabel("ส่วนสูง (เซนติเมตร)")

        self.height_input = QLineEdit()

        self.height_input.setPlaceholderText(
            "กรอกส่วนสูง"
        )

        # ===== ปุ่มคำนวณ =====
        self.calculate_button = QPushButton(
            "💚คำนวณ BMI"
        )

        # ===== เพิ่ม Widget =====
        layout.addWidget(weight_label)

        layout.addWidget(self.weight_input)

        layout.addWidget(height_label)

        layout.addWidget(self.height_input)

        layout.addWidget(self.calculate_button)

        # ===== ตั้ง Layout =====
        self.setLayout(layout)