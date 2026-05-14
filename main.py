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

        self.setStyleSheet("""
        /* พื้นหลังหน้าต่าง */
        QMainWindow, QWidget {
            background-color: #F7F9F8;
            font-family: 'Segoe UI', 'Kanit';
        }

        /* หัวข้อช่องกรอก */
        QLabel {
            color: #2D6A4F;
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 2px;
        }

        /* ช่องกรอกข้อมูล */
        QLineEdit {
            background-color: #FFFFFF;
            border: 2px solid #E0E0E0;
            border-radius: 12px;
            padding: 12px;
            font-size: 15px;
            color: #333333;
        }

        QLineEdit:focus {
            border: 2px solid #74C69D;
        }

        /* ปุ่มหลัก */
        QPushButton {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 #74C69D, stop:1 #40916C);
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 15px;
            padding: 15px;
        }

        QPushButton:hover {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 #95D5B2, stop:1 #52B788);
        }

        /* ปุ่มประวัติ */
        QPushButton#history_button {
            background-color: #D8F3DC;
            color: #2D6A4F;
            font-size: 14px;
            border: 1px solid #B7E4C7;
        }

        /* --- จุดที่แก้ไข: QComboBox (เพิ่มปิดปีกกาให้ครบ) --- */
        QComboBox {
            background-color: #FFFFFF;
            border: 2px solid #E0E0E0;
            border-radius: 12px;
            padding: 10px;
            font-size: 15px;
            color: #333333;
        } /* <--- ตัวนี้แหละที่หายไป */

        QComboBox::drop-down {
            border: none;
            width: 30px;
        }

        QAbstractItemView {
            background-color: #FFFFFF;
            selection-background-color: #74C69D;
            selection-color: white;
        }

        /* --- แถม: สไตล์สำหรับ RadioButton (แบบจุด) --- */
        QRadioButton {
            font-size: 15px;
            color: #2D6A4F;
            spacing: 8px;
        }
        
        QRadioButton::indicator {
            width: 18px;
            height: 18px;
        }

        QRadioButton::indicator:checked {
            image: url(none); /* หรือใส่รูปจุดถ้ามี */
            background-color: #40916C;
            border: 2px solid #D8F3DC;
            border-radius: 9px;
        }
        
        QRadioButton::indicator:unchecked {
            background-color: white;
            border: 2px solid #E0E0E0;
            border-radius: 9px;
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
            # 1. ดึงค่าชื่อจากช่องกรอกชื่อ
            name = self.input_page.name_input.text().strip()
            if not name:
                name = "ไม่ระบุชื่อ" # ป้องกันถ้าไม่ได้กรอกชื่อมา

            # เช็คว่าถ้าปุ่ม "ชาย" ถูกติ๊ก ให้ gender เป็น "ชาย" ถ้าไม่ติ๊กก็เป็น "หญิง"
            if self.input_page.male_radio.isChecked():
                gender = "ชาย"
            else:
                gender = "หญิง"

            # 2. ดึงค่าตัวเลข
            weight_str = self.input_page.weight_input.text()
            height_str = self.input_page.height_input.text()

            # ตรวจสอบว่ากรอกตัวเลขครบไหม
            if not weight_str or not height_str:
                QMessageBox.warning(self, "ข้อมูลไม่ครบ", "กรุณากรอกน้ำหนักและส่วนสูง")
                return

            weight = float(weight_str)
            height = float(height_str)

            # ป้องกันส่วนสูงเป็น 0 (หารด้วยศูนย์ไม่ได้)
            if height <= 0:
                QMessageBox.warning(self, "ข้อมูลไม่ถูกต้อง", "ส่วนสูงต้องมากกว่า 0")
                return

            # 3. คำนวณ (เรียกใช้ไฟล์ bmi_calculator.py)
            bmi = BMICalculator.calculate(weight, height)

            if bmi is None:
               raise Exception("BMI is None")

            status, advice, link = HealthAdvisor.get_advice(bmi, gender)

            # 4. บันทึกข้อมูล (ใช้ชื่อที่ดึงมาแทน "User")
            self.db.insert(name, gender, weight, height, bmi, status)
            self.result_page.gender_display.setText(f"เพศ: {gender}") # บรรทัดนี้แหละ!
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

        except ValueError:
            QMessageBox.warning(self, "ข้อมูลไม่ถูกต้อง", "กรุณากรอกน้ำหนักและส่วนสูงเป็นตัวเลขเท่านั้น")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"เกิดข้อผิดพลาด: {str(e)}")

    # =========================
    # ประวัติ
    # =========================
    def show_history(self):
        try:
           data = self.db.get_all()

           text = "📜 ประวัติการคำนวณ BMI\n\n"

           for row in data:
                _, name, gender, weight, height, bmi, status = row
                text += f"{name}, เพศ{gender} | {weight}kg | {height}cm | BMI {bmi:.2f} | {status}\n"

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