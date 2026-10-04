def calculate_grade(marks: float) -> str:
    """
    Calculates the letter grade based on marks.
    Grade A: 80 - 100
    Grade B: 70 - 79
    Grade C: 60 - 69
    Grade D: 50 - 59
    Grade F: Below 50
    """
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def calculate_total_marks(marks: float, bonus: float = 5.0) -> float:
    """Calculates total marks including any bonus points."""
    return marks + bonus
