from database import create_connection


def add_student(name, age, major):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
            (name, age, major),
        )


def add_course(course_name, instructor):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO courses (course_name, instructor) VALUES (?, ?)",
            (course_name, instructor),
        )

def enroll_student(student_id, course_id):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO student_courses (student_id, course_id) VALUES (?, ?)",
            (student_id, course_id),
        )

def get_students():
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()


def get_courses():
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()
def get_students_in_course(course_id):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT students.id, students.name
            FROM students
            JOIN student_courses
                ON students.id = student_courses.student_id
            WHERE student_courses.course_id = ?
        """, (course_id,))
        return cursor.fetchall()