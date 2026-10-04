import json
from pathlib import Path

from config import APP_NAME, DEBUG, MAX_STUDENTS
from logger import logger
from services.calculator import calculate_grade, calculate_total_marks
from utils.validation import validate_marks, validate_name


def load_student_data(filename: str = "student.json") -> dict:
    """Loads and returns student data from the data directory with exception handling."""
    base_dir = Path(__file__).resolve().parent.parent.parent
    data_path = base_dir / "data" / filename

    if not data_path.exists():
        data_path = Path("data") / filename

    try:
        with open(data_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info("Successfully loaded student data from %s", data_path)
            return data
    except FileNotFoundError:
        logger.error("Data file not found at %s", data_path)
        raise
    except json.JSONDecodeError as e:
        logger.error("Failed to parse JSON file: %s", e)
        raise


def display_config():
    """Displays application configuration."""
    print("=" * 45)
    print(f"Application Name : {APP_NAME}")
    print(f"Debug Mode       : {DEBUG}")
    print(f"Maximum Students : {MAX_STUDENTS}")
    print("=" * 45)


def display_report(student: dict, total_marks: float, grade: str):
    """Outputs formatted student report."""
    print("\n---------------- STUDENT REPORT ----------------")
    print(f"ID          : {student.get('id', 'N/A')}")
    print(f"Name        : {student.get('name')}")
    print(f"Program     : {student.get('program', 'N/A')}")
    print(f"Semester    : {student.get('semester', 'N/A')}")
    print(f"Base Marks  : {student.get('marks')}")
    print(f"Total Marks : {total_marks}")
    print(f"Final Grade : {grade}")
    print("------------------------------------------------")


def main():
    logger.info("Starting %s application", APP_NAME)

    # 1. Display environment configuration
    display_config()

    # 2. Load student input (separated responsibility with exception handling)
    try:
        student = load_student_data()
    except Exception as e:
        logger.error("Application aborted due to data loading failure: %s", e)
        print(f"Error: Unable to load student data ({e})")
        return

    # 3. Validation (separated responsibility)
    name = student.get("name", "")
    marks = student.get("marks")

    if not validate_name(name):
        logger.warning("Validation failed: Invalid student name '%s'", name)
        print("Error: Invalid student name in records.")
        return

    if not validate_marks(marks):
        logger.warning("Validation failed: Invalid marks '%s'", marks)
        print("Error: Marks must be between 0 and 100.")
        return

    # 4. Calculation (separated responsibility)
    total_marks = calculate_total_marks(marks, bonus=5)
    grade = calculate_grade(marks)
    logger.info("Calculations complete: total=%s, grade=%s", total_marks, grade)

    # 5. Output / Application Flow
    display_report(student, total_marks, grade)
    logger.info("Application executed successfully.")


if __name__ == "__main__":
    main()