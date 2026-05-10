# =========================
# bmi_calculator.py
# =========================

class BMICalculator:

    @staticmethod
    def calculate(weight, height):

        # แปลง cm เป็น m
        height_m = height / 100

        # สูตร BMI
        bmi = weight / (height_m ** 2)

        return bmi