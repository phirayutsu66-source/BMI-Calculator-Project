# =========================
# main.py
# =========================

import sys
from database import Database
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
from history_page import HistoryPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.input_page = InputPage()
        self.result_page = ResultPage()
        self.history_page = HistoryPage()
        # ตั้งชื่อโปรแกรม
        self.setWindowTitle("โปรแกรมคำนวณ BMI")

        # ขนาดหน้าต่าง
        self.resize(400, 300)

        self.db = Database()

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

        self.stack.addWidget(self.input_page)   # index 0
        self.stack.addWidget(self.result_page)  # index 1
        self.stack.addWidget(self.history_page) # index 2

        self.setCentralWidget(self.stack)

        # ===== ปุ่ม =====
        self.input_page.calculate_button.clicked.connect(self.calculate_bmi)
        self.result_page.back_button.clicked.connect(self.go_back)
        self.input_page.history_button.clicked.connect(self.show_history)
        self.history_page.back_button.clicked.connect(self.go_back)

    def go_back(self):
        self.stack.setCurrentWidget(self.input_page)

        
    # =========================
    # คำนวณ BMI
    # =========================
    def calculate_bmi(self):
        print("test")

        try:
            weight = float(self.input_page.weight_input.text())
            height = float(self.input_page.height_input.text())

            if weight <= 0 or height <= 0:
                QMessageBox.warning(self, "ข้อผิดพลาด", "กรุณากรอกค่ามากกว่า 0")
                return

            bmi = BMICalculator.calculate(weight, height)
            status, advice, link = HealthAdvisor.get_advice(bmi)

            if status == "ผอม":
                self.result_page.result_label.setStyleSheet("""
                color: #2196F3;
                font-size: 20px;
                font-weight: bold;
                """)

            elif status == "ปกติ":
                self.result_page.result_label.setStyleSheet("""
                color: #2E7D32;
                font-size: 20px;
                font-weight: bold;
                """)

            else:
                self.result_page.result_label.setStyleSheet("""
                color: #D32F2F;
                font-size: 20px;
                font-weight: bold;
                """)

            self.result_page.result_label.setText(
                f"ค่า BMI : {bmi:.2f}\nสถานะ : {status}"
            )

            self.result_page.advice_label.setText(advice)
            self.result_page.link_label.setText(f'<a href="{link}">อ่านเพิ่มเติม</a>')

            self.stack.setCurrentWidget(self.result_page)

        except:
            QMessageBox.warning(self, "ข้อมูลไม่ถูกต้อง", "กรุณากรอกตัวเลขให้ถูกต้อง")

    # =========================
    # ประวัติ
    # =========================
    def show_history(self):
        try:
           data = self.db.get_all()

           text = "📜 ประวัติการคำนวณ BMI\n\n"

           for row in data:
                _, name, weight, height, bmi, status = row
                text += f"{name} | {weight}kg | {height}cm | BMI {bmi:.2f} | {status}\n"

           self.history_page.history_label.setText(text)

        # ใช้ index แทน widget (ชัวร์กว่า)
           self.stack.setCurrentIndex(2)

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
     
        

# =========================
# เปิดโปรแกรม
# =========================
app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()