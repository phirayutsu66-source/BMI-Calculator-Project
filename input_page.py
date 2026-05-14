from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,    # เพิ่มตัวนี้เพื่อจัดปุ่มแนวนอน
    QRadioButton    # เปลี่ยนจาก QComboBox เป็น QRadioButton
)

class InputPage(QWidget):
    def __init__(self):
        super().__init__()

        # ===== Layout หลัก =====
        layout = QVBoxLayout()

        # ===== ชื่อ =====
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("กรอกชื่อ")
        name_label = QLabel("ชื่อ")

        # ===== เพศ (เปลี่ยนเป็นแบบจุด Radio Button) =====
        gender_label = QLabel("เพศ")
        
        # สร้าง Layout แนวนอนสำหรับวางจุด ชาย-หญิง
        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("ชาย")
        self.female_radio = QRadioButton("หญิง")
        self.male_radio.setChecked(True)  # ตั้งให้เลือก "ชาย" ไว้ก่อนเป็นค่าเริ่มต้น
        
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        
        # สร้าง Widget มาครอบกลุ่มจุดไว้เพื่อให้ใส่ลง Layout หลักได้
        gender_group_widget = QWidget()
        gender_group_widget.setLayout(gender_layout)

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

        # ===== ปุ่มประวัติ =====
        self.history_button = QPushButton("📜 ดูประวัติ")

        # ===== เพิ่ม Widget เข้า Layout หลัก =====
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        layout.addWidget(gender_label)
        layout.addWidget(gender_group_widget) # ใส่กลุ่มของ "จุดเลือก" ลงไปตรงนี้

        layout.addWidget(weight_label)
        layout.addWidget(self.weight_input)

        layout.addWidget(height_label)
        layout.addWidget(self.height_input)

        layout.addWidget(self.calculate_button)
        layout.addWidget(self.history_button)

        # ===== ตั้ง Layout =====
        self.setLayout(layout)