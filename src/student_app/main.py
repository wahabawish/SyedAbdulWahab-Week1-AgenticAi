import json
from pathlib import Path

from config import APP_NAME, DEBUG, MAX_STUDENTS
from Calculators import GradeCalculators
from Reportings import Reportings


def load_student_data():
    # Locate data/student.json reliably regardless of current working directory
    base_dir = Path(__file__).resolve().parent.parent.parent
    json_path = base_dir / "data" / "student.json"
    if not json_path.exists():
        json_path = Path("data/student.json")

    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    # 1. Display Configuration from .env
    print("=" * 40)
    print(f"Application Name : {APP_NAME}")
    print(f"Debug Mode       : {DEBUG}")
    print(f"Maximum Students : {MAX_STUDENTS}")
    print("=" * 40)

    # 2. Load JSON data into Python dictionary
    student = load_student_data()

    print("\n--- Loaded Student Details (JSON) ---")
    print(f"Student ID : {student['id']}")
    print(f"Name       : {student['name']}")
    print(f"Program    : {student['program']}")
    print(f"Semester   : {student['semester']}")
    print(f"Marks      : {student['marks']}")

    # 3. Combine with calculations and reporting
    bonus = 5
    total_marks = student["marks"] + bonus
    grade = GradeCalculators(student["marks"])

    Reportings(student["name"], total_marks, student["marks"], grade)


if __name__ == "__main__":
    main()