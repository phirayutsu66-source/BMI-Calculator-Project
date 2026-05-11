# =========================
# main.py
# =========================

import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QMessageBox
)

from input_page import InputPage
from result_page import ResultPage
from bmi_calculator import BMICalculator
from health_advisor import HealthAdvisor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # ตั้งชื่อโปรแกรม
        self.setWindowTitle(
            "โปรแกรมคำนวณ BMI"
        )

        # ขนาดหน้าต่าง
        self.resize(400, 300)

        # =========================
        # BMI Theme Style
        # =========================
        self.setStyleSheet("""

        QMainWindow {
            background-color: #EAF7F0;
        }

        QWidget {
            background-color: #EAF7F0;
            font-family: Segoe UI;
        }

        QLabel {
            color: #1B4332;
            font-size: 16px;
            font-weight: bold;
        }

        QLineEdit {
            background-color: white;
            border: 2px solid #95D5B2;
            border-radius: 12px;
            padding: 10px;
            font-size: 14px;
            color: #333333;
        }

        QLineEdit:focus {
            border: 2px solid #2D6A4F;
        }

        QPushButton {
            background-color: #2D6A4F;
            color: white;
            font-size: 15px;
            font-weight: bold;
            border-radius: 12px;
            padding: 12px;
        }

        QPushButton:hover {
            background-color: #40916C;
        }

        QPushButton:pressed {
            background-color: #1B4332;
        }

        """)

        # ===== Stacked Widget =====
        self.stack = QStackedWidget()
        # ===== สร้าง stacked widget =====
        self.stack = QStackedWidget()

        # ===== สร้างหน้า =====
        self.input_page = InputPage()

        self.result_page = ResultPage()

        # ===== เพิ่มหน้า =====
        self.stack.addWidget(
            self.input_page
        )

        self.stack.addWidget(
            self.result_page
        )

        # ===== ตั้งหน้าหลัก =====
        self.setCentralWidget(
            self.stack
        )

        # ===== ปุ่มคำนวณ =====
        self.input_page.calculate_button.clicked.connect(
            self.calculate_bmi
        )

        # ===== ปุ่มย้อนกลับ =====
        self.result_page.back_button.clicked.connect(
            self.go_back
        )

    # =========================
    # คำนวณ BMI
    # =========================
    def calculate_bmi(self):
            # =========================
        try:
            # รับค่าน้ำหนัก
            weight = float(
                self.input_page.weight_input.text()
            )

            # รับค่าส่วนสูง
            height = float(
                self.input_page.height_input.text()
            )

            # ตรวจสอบข้อมูล
            if weight <= 0 or height <= 0:

                QMessageBox.warning(
                    self,
                    "ข้อผิดพลาด",
                    "กรุณากรอกค่ามากกว่า 0"
                )

                return

            # คำนวณ BMI
            bmi = BMICalculator.calculate(
                weight,
                height
            )

            # รับคำแนะนำ + ลิงก์
            status, advice, link = HealthAdvisor.get_advice(
                bmi
            )  # รับคำแนะนำ + ลิงก์
            status, advice, link = HealthAdvisor.get_advice(
                bmi
            )
            # เปลี่ยนสีตามสถานะ BMI
            if status == "ผอม":

                self.result_page.result_label.setStyleSheet(
                    """
                    color: #2196F3;
                    font-size: 20px;
                    font-weight: bold;
                    """
                )

            elif status == "ปกติ":

                self.result_page.result_label.setStyleSheet(
                    """
                    color: #2E7D32;
                    font-size: 20px;
                    font-weight: bold;
                    """
                )

            else:

                self.result_page.result_label.setStyleSheet(
                    """
                    color: #D32F2F;
                    font-size: 20px;
                    font-weight: bold;
                    """
                )
        

            # แสดงผลลัพธ์
            self.result_page.result_label.setText(
                f"ค่า BMI : {bmi:.2f}\nสถานะ : {status}"
            )

            # แสดงคำแนะนำ
            self.result_page.advice_label.setText(
                advice
            )

            # เปลี่ยนลิงก์
            self.result_page.link_label.setText(
                f'<a href="{link}">อ่านเพิ่มเติม</a>'
            )

            # เปลี่ยนหน้า
            self.stack.setCurrentWidget(
                self.result_page
            )

        except:

            QMessageBox.warning(
                self,
                "ข้อมูลไม่ถูกต้อง",
                "กรุณากรอกตัวเลขให้ถูกต้อง"
            )
    
    # =========================
    # กลับหน้าแรก
    # =========================
    def go_back(self):

        self.stack.setCurrentWidget(
            self.input_page
        )
        

# =========================
# เปิดโปรแกรม
# =========================
app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()