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

        # ===== ชื่อ =====
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("กรอกชื่อ")
        name_label = QLabel("ชื่อ")

        # ===== น้ำหนัก =====
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("กรอกน้ำหนัก")
        weight_label = QLabel("น้ำหนัก (กิโลกรัม)")

        # ===== ส่วนสูง =====
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("กรอกส่วนสูง")
        height_label = QLabel("ส่วนสูง (เซนติเมตร)")

        # ===== ปุ่มคำนวณ =====
        self.calculate_button = QPushButton("💚คำนวณ BMI")



        self.history_button = QPushButton("📜 ดูประวัติ")

        # ===== เพิ่ม Widget =====
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        layout.addWidget(weight_label)
        layout.addWidget(self.weight_input)

        layout.addWidget(height_label)
        layout.addWidget(self.height_input)

        layout.addWidget(self.calculate_button)

        layout.addWidget(self.history_button)

        # ===== ตั้ง Layout =====
        self.setLayout(layout)