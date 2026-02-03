from models import (
    add_student,
    add_course,
    get_students,
    get_courses,
    enroll_student,
    get_students_in_course,
)
from database import create_tables


def print_students(students):
    if not students:
        print("Студентів немає.")
        return
    for s in students:
        print(f"ID: {s[0]} | Імʼя: {s[1]} | Вік: {s[2]} | Спеціальність: {s[3]}")


def print_courses(courses):
    if not courses:
        print("Курсів немає.")
        return
    for c in courses:
        print(f"ID: {c[0]} | Назва: {c[1]} | Інструктор: {c[2]}")


def main_menu():
    create_tables()

    while True:
        print("\n--- Student Journal ---")
        print("1. Додати студента")
        print("2. Додати курс")
        print("3. Переглянути студентів")
        print("4. Переглянути курси")
        print("5. Записати студента на курс")
        print("6. Список студентів на курсі")
        print("0. Вихід")

        choice = input("Вибір: ")

        try:
            if choice == "1":
                name = input("Імʼя: ")
                age = int(input("Вік: "))
                major = input("Спеціальність: ")
                add_student(name, age, major)
                print("✅ Студент доданий!")

            elif choice == "2":
                course_name = input("Назва курсу: ")
                instructor = input("Інструктор: ")
                add_course(course_name, instructor)
                print("✅ Курс доданий!")

            elif choice == "3":
                print_students(get_students())

            elif choice == "4":
                print_courses(get_courses())

            elif choice == "5":
                student_id = int(input("ID студента: "))
                course_id = int(input("ID курсу: "))
                enroll_student(student_id, course_id)
                print("✅ Студента записано на курс!")

            elif choice == "6":
                course_id = int(input("ID курсу: "))
                students = get_students_in_course(course_id)
                if not students:
                    print("На курсі поки немає студентів.")
                else:
                    print("Студенти на курсі:")
                    for s in students:
                        print(f"ID: {s[0]} | Імʼя: {s[1]}")

            elif choice == "0":
                print("Вихід...")
                break

            else:
                print("Невірний вибір!")

        except ValueError:
            print("❗ Помилка вводу. Перевірте дані.")


if __name__ == "__main__":
    create_tables()
    main_menu()
