# BMI-Calculator-Project
# 🏥 BMI Calculator Project (PySide6 + SQLite)

โปรแกรมคำนวณดัชนีมวลกาย (BMI) ที่พัฒนาขึ้นด้วยภาษา **Python** โดยเน้นการออกแบบที่ใช้งานง่าย และมีระบบบันทึกข้อมูลย้อนหลัง

## 🚀 จุดเด่นของโปรเจกต์ (Key Features)
* **Smart Calculation:** คำนวณค่า BMI ตามมาตรฐานสากล พร้อมระบบวิเคราะห์สุขภาพอัตโนมัติ
* **Dynamic UI:** หน้าจอแสดงผลมีการเปลี่ยนสีตามสถานะสุขภาพ (Blue/Green/Red) เพื่อให้เข้าใจง่าย
* **Database Integration:** มีระบบจัดเก็บประวัติการคำนวณด้วย **SQLite** สามารถดูย้อนหลังได้
* **Robust Logic:** มีการดักจับข้อผิดพลาด (Error Handling) ป้องกันโปรแกรมค้างจากการกรอกข้อมูลผิด

## 🛠️ เทคนิคที่ใช้ (Technical Stack)
* **GUI Framework:** PySide6
* **Core Logic:** Python OOP (Class & Static Methods)
* **Database:** SQLite3 (SQL INSERT/SELECT operations)
* **Design Tools:** Canva & Whimsical

## 📂 โครงสร้างโค้ดที่สำคัญ
* **ส่วนคำนวณ:** ใช้ `if-elif-else` เพื่อจำแนกประเภท BMI และให้คำแนะนำ
* **ส่วนความปลอดภัย:** ใช้ `try-except` เพื่อจัดการกับ `ValueError`
* **ส่วนบันทึกข้อมูล:** ใช้คำสั่ง SQL `INSERT INTO` พร้อม `self.conn.commit()` เพื่อบันทึกข้อมูลถาวร

## 👨‍💻 ผู้จัดทำ
**นายพีรยุทธ สุโภภาค** (66114640699)
นักศึกษาคณะเทคโนโลยีอุตสาหกรรม
เสนอ: **อาจารย์ ณัฐวุฒิ บรรเรือนทอง**
