import sqlite3

def connect_db():
    conn = sqlite3.connect('student.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hours REAL,
        attendance REAL,
        predicted_marks REAL
    )
    ''')

    conn.commit()
    conn.close()


def insert_data(hours, attendance, marks):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO students (hours, attendance, predicted_marks)
    VALUES (?, ?, ?)
    ''', (hours, attendance, marks))

    conn.commit()
    conn.close()
    
    
def fetch_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()
    return rows