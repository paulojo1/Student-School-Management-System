"""Load and save students using a JSON file."""
import json
import os

from student import Student

DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "students.json")


def load_students():
    """Read students from the file. Returns an empty list if there is none."""
    students = []
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No data file yet - starting fresh.")
    except json.JSONDecodeError:
        print("Data file is damaged - starting fresh.")
    else:
        for item in data:
            students.append(Student(**item))
    finally:
        print(f"{len(students)} student(s) loaded.")
    return students


def save_students(students):
    """Write all students to the file."""
    try:
        os.makedirs(DATA_FOLDER, exist_ok=True)
        with open(DATA_FILE, "w") as file:
            json.dump([s.to_dict() for s in students], file, indent=4)
    except OSError as error:
        print("Could not save data:", error)
