"""Student Result Management System - run this file to start."""
import re
from datetime import datetime

import reports
import results
import storage
from student import Student


def find_student(students, student_id):
    for s in students:
        if s.student_id == student_id:
            return s
    return None


def add_student(students):
    student_id = input("Student ID: ").strip()
    if student_id == "":
        print("ID cannot be empty.")
        return
    if find_student(students, student_id) is not None:
        print("That ID already exists.")
        return
    name = input("Full name: ").strip()
    student_class = input("Class: ").strip()
    gender = input("Gender (M/F): ").strip().upper()
    dob = input("Date of birth (YYYY-MM-DD): ").strip()
    # Regular expression: 4 digits - 2 digits - 2 digits
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", dob):
        print("Invalid date. Use the format 2008-04-12.")
        return
    students.append(Student(student_id, name, student_class, gender, dob))
    storage.save_students(students)
    print("Student added.")


def view_all(students):
    if len(students) == 0:
        print("No students yet.")
    for s in students:
        print(f"{s.student_id:<10}{s.name:<22}{s.student_class:<8}"
              f"{s.gender:<4}{s.dob}")


def search_student(students):
    term = input("Search by ID or name: ").strip().lower()
    found = False
    for s in students:
        if term == s.student_id.lower() or term in s.name.lower():
            print(f"{s.student_id:<10}{s.name:<22}{s.student_class:<8}"
                  f"{s.gender:<4}{s.dob}")
            found = True
    if not found:
        print("No match found.")


def update_student(students):
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    print("Press Enter to keep the old value.")
    s.name = input(f"Name [{s.name}]: ").strip() or s.name
    s.student_class = input(f"Class [{s.student_class}]: ").strip() or s.student_class
    s.gender = input(f"Gender [{s.gender}]: ").strip().upper() or s.gender
    storage.save_students(students)
    print("Student updated.")


def delete_student(students):
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    if input(f"Delete {s.name}? (y/n): ").lower() == "y":
        students.remove(s)
        storage.save_students(students)
        print("Student deleted.")


def record_scores(students):
    """Record scores, or update them if they already exist."""
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
        return
    for subject in results.SUBJECTS:
        old = s.scores.get(subject)
        while True:
            text = input(f"{subject} (0-100): ").strip()
            if text == "" and old is not None:
                break  # keep the old score
            try:
                score = float(text)
            except ValueError:
                print("Please enter a number.")
            else:
                if 0 <= score <= 100:
                    s.scores[subject] = score
                    break
                print("Score must be between 0 and 100.")
    s.date_entered = datetime.now().strftime("%Y-%m-%d %H:%M")
    storage.save_students(students)
    print("Scores saved.")


def show_report_card(students):
    s = find_student(students, input("Student ID: ").strip())
    if s is None:
        print("Student not found.")
    else:
        print(reports.report_card(s))


def list_results(students):
    choice = input("Sort by 1) average or 2) name: ").strip()
    if choice == "2":
        ordered = sorted(students, key=lambda s: s.name.lower())
    else:
        ordered = sorted(students,
                         key=lambda s: results.get_average(s.scores),
                         reverse=True)
    print(reports.results_table(ordered))


def show_stats(students):
    stats = results.class_stats(students)
    if stats is None:
        print("No scores recorded yet.")
    else:
        highest, lowest, average = stats
        print(f"Highest total: {highest:.1f}")
        print(f"Lowest total : {lowest:.1f}")
        print(f"Class average: {average:.2f}")


def main():
    students = storage.load_students()
    while True:
        print("\n=== STUDENT RESULT SYSTEM ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Record / update scores")
        print("7. Show report card")
        print("8. List results (sorted)")
        print("9. Class statistics")
        print("10. Save text report")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            record_scores(students)
        elif choice == "7":
            show_report_card(students)
        elif choice == "8":
            list_results(students)
        elif choice == "9":
            show_stats(students)
        elif choice == "10":
            print("Report saved to", reports.save_report(students))
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


main()
