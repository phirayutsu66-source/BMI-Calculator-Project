# =========================
# health_advisor.py
# =========================

class HealthAdvisor:

    @staticmethod
    def get_advice(bmi, gender):

        # ===== กรณีผู้ชาย =====
        if gender == "ชาย":
            if bmi < 18.5:
                status = "ผอม"
                advice = "- ควรเน้นทานโปรตีนเพื่อเสริมสร้างมวลกล้ามเนื้อ\n- ออกกำลังกายแบบแรงต้าน (Weight Training)\n- พักผ่อนให้เพียงพอ"
                link = "https://thonburimedicalcenter.com/th/blog/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B2%E0%B8%A3/Underweight-5-healthy-tips-to-gain-weight-and-build-muscle-mass"
            elif bmi < 25:
                status = "ปกติ"
                advice = "- สุขภาพอยู่ในเกณฑ์ดีสำหรับผู้ชาย\n- เน้นการรักษาความฟิตของร่างกาย\n- ดื่มน้ำให้เพียงพอ"
                link = "https://www.doctoryokoweightloss.com/blog/10189/7-%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5-%E0%B8%A3%E0%B8%B1%E0%B8%81%E0%B8%A9%E0%B8%B2%E0%B8%AB%E0%B8%B8%E0%B9%88%E0%B8%99%E0%B8%9B%E0%B8%B1%E0%B8%87-%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%81%E0%B8%A5%E0%B8%B1%E0%B8%9A%E0%B9%84%E0%B8%9B%E0%B8%9E%E0%B8%B1%E0%B8%87%E0%B8%AD%E0%B8%B5%E0%B8%81"
            else:
                status = "อ้วน"
                advice = "- ระวังเรื่องไขมันสะสมบริเวณหน้าท้อง (ลงพุง)\n- ลดอาหารหวานและของมัน\n- ออกกำลังกายแบบคาร์ดิโอสม่ำเสมอ"
                link = "https://www.bangkokhospital.com/th/bangkok/content/secret-recipe-define-food-for-weight-loss"

        # ===== กรณีผู้หญิง =====
        else:
            if bmi < 18.5:
                status = "ผอม"
                advice = "- ระวังเรื่องมวลกระดูกและสารอาหารที่จำเป็น\n- ทานอาหารที่มีธาตุเหล็กและแคลเซียมเพิ่มขึ้น\n- พักผ่อนให้เพียงพอ"
                link = "https://thonburimedicalcenter.com/th/blog/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B8%B9%E0%B8%A5%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A7%E0%B8%AA%E0%B8%B2%E0%B8%A3/Underweight-5-healthy-tips-to-gain-weight-and-build-muscle-mass"
            elif bmi < 25:
                status = "ปกติ"
                advice = "- สุขภาพสมส่วนดีสำหรับผู้หญิง\n- ทานอาหารที่มีกากใยและเน้นผักผลไม้\n- ออกกำลังกายเพื่อความกระชับ"
                link = "https://www.doctoryokoweightloss.com/blog/10189/7-%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5-%E0%B8%A3%E0%B8%B1%E0%B8%81%E0%B8%A9%E0%B8%B2%E0%B8%AB%E0%B8%B8%E0%B9%88%E0%B8%99%E0%B8%9B%E0%B8%B1%E0%B8%87-%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B8%81%E0%B8%A5%E0%B8%B1%E0%B8%9A%E0%B9%84%E0%B8%9B%E0%B8%9E%E0%B8%B1%E0%B8%87%E0%B8%AD%E0%B8%B5%E0%B8%81"
            else:
                status = "อ้วน"
                advice = "- ระวังเรื่องระดับน้ำตาลและไขมันสะสมตามสัดส่วน\n- ควบคุมการทานแป้งและของมัน\n- ออกกำลังกายเน้นการเผาผลาญ"
                link = "https://www.bangkokhospital.com/th/bangkok/content/secret-recipe-define-food-for-weight-loss"

        return status, advice, link