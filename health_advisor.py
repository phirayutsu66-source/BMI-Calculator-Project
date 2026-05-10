# =========================
# health_advisor.py
# =========================

class HealthAdvisor:

    @staticmethod
    def get_advice(bmi):

        # ===== ผอม =====
        if bmi < 18.5:

            status = "ผอม"

            advice = """
- ควรรับประทานอาหารให้ครบ 5 หมู่
- พักผ่อนให้เพียงพอ
- ออกกำลังกายเพื่อเพิ่มกล้ามเนื้อ
"""

            link = "https://thonburimedicalcenter.com/th/blog/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B2%E0%B8%A3/Underweight-5-healthy-tips-to-gain-weight-and-build-muscle-mass"

        # ===== ปกติ =====
        elif bmi < 25:

            status = "ปกติ"

            advice = """
- สุขภาพอยู่ในเกณฑ์ปกติ
- ออกกำลังกายสม่ำเสมอ
- ดื่มน้ำให้เพียงพอ
"""

            link = "https://www.cdc.gov/bmi/index.html"

        # ===== อ้วน =====
        else:

            status = "อ้วน"

            advice = """
- ควรลดอาหารหวานและของมัน
- ออกกำลังกายอย่างสม่ำเสมอ
- ควบคุมน้ำหนักอย่างต่อเนื่อง
"""

            link = "https://www.siphhospital.com"

        return status, advice, link