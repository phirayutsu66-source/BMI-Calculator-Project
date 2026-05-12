import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("bmi.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            weight REAL,
            height REAL,
            bmi REAL,
            status TEXT
        )
        """)
        self.conn.commit()

    def insert(self, name, weight, height, bmi, status):
        self.cursor.execute("""
        INSERT INTO bmi_history (name, weight, height, bmi, status)
        VALUES (?, ?, ?, ?, ?)
        """, (name, weight, height, bmi, status))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM bmi_history")
        return self.cursor.fetchall()