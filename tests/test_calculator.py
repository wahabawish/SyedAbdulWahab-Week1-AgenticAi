import sys
from pathlib import Path

# Ensure src/ is on sys.path for test imports
src_dir = Path(__file__).resolve().parent.parent / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from student_app.services.calculator import calculate_grade, calculate_total_marks


def test_grade_a():
    """Test Grade A for 85 marks."""
    assert calculate_grade(85) == "A"


def test_grade_b():
    """Test Grade B for 75 marks."""
    assert calculate_grade(75) == "B"


def test_grade_c():
    """Test Grade C for 65 marks."""
    assert calculate_grade(65) == "C"


def test_grade_d():
    """Test Grade D for 55 marks."""
    assert calculate_grade(55) == "D"


def test_grade_f():
    """Test Grade F for 40 marks."""
    assert calculate_grade(40) == "F"


def test_calculate_total_marks():
    """Test bonus calculation."""
    assert calculate_total_marks(85, bonus=5) == 90
