from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)
from PySide6.QtCore import Qt  # ต้องมีตัวนี้ด้วยสำหรับ Qt.AlignCenter


class ResultPage(QWidget):
    def __init__(self):
        super().__init__()

        # ===== Layout =====
        layout = QVBoxLayout()

        # ===== ส่วนแสดงเพศ (เพิ่มใหม่) =====
        self.gender_display = QLabel("เพศ: -")
        self.gender_display.setAlignment(Qt.AlignCenter)
        self.gender_display.setStyleSheet("""
            color: #666666;
            font-size: 14px;
            font-weight: normal;
        """)

        # ===== ผลลัพธ์ BMI =====
        self.result_label = QLabel("ผลลัพธ์ BMI")
        self.result_label.setAlignment(Qt.AlignCenter)

        # ===== คำแนะนำ =====
        self.advice_label = QLabel("คำแนะนำสุขภาพ")
        self.advice_label.setAlignment(Qt.AlignCenter)

        # ===== ลิงก์อ่านเพิ่มเติม =====
        self.link_label = QLabel()
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setAlignment(Qt.AlignCenter)

        # ===== ปุ่มย้อนกลับ =====
        self.back_button = QPushButton("◀️ย้อนกลับ")

        # ===== เพิ่ม Widget ลง Layout (เอาเพศไว้บนสุดหรือใต้ BMI ก็ได้) =====
        layout.addWidget(self.gender_display) # <--- โชว์เพศตรงนี้
        layout.addWidget(self.result_label)
        layout.addWidget(self.advice_label)
        layout.addWidget(self.link_label)
        layout.addWidget(self.back_button)

        # ===== ตั้ง Layout =====
        self.setLayout(layout)