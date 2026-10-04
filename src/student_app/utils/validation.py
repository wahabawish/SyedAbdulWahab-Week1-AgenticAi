def validate_marks(marks) -> bool:
    """
    Validates student marks.
    Marks must be a number between 0 and 100 inclusive.
    """
    if not isinstance(marks, (int, float)):
        return False
    if marks < 0 or marks > 100:
        return False
    return True


def validate_name(name: str) -> bool:
    """
    Validates student name.
    Name must be a non-empty string.
    """
    if not isinstance(name, str):
        return False
    return bool(name.strip())
