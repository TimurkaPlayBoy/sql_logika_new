import sqlite3

def create_connection():
    conn = sqlite3.connect("students.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        instructor TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY(student_id, course_id),
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(course_id) REFERENCES courses(course_id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()