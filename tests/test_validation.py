import sys
from pathlib import Path

# Ensure src/ is on sys.path for test imports
src_dir = Path(__file__).resolve().parent.parent / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from student_app.utils.validation import validate_marks, validate_name


def test_valid_marks():
    """Test valid marks within 0-100 range."""
    assert validate_marks(85) is True
    assert validate_marks(50) is True


def test_invalid_marks_negative():
    """Test invalid marks below 0."""
    assert validate_marks(-1) is False
    assert validate_marks(-50) is False


def test_invalid_marks_exceeding_max():
    """Test invalid marks above 100."""
    assert validate_marks(101) is False
    assert validate_marks(150) is False


def test_boundary_conditions():
    """Test boundary conditions (0 and 100 are valid)."""
    assert validate_marks(0) is True
    assert validate_marks(100) is True


def test_invalid_data_types():
    """Test non-numeric inputs."""
    assert validate_marks("eighty") is False
    assert validate_marks(None) is False


def test_validate_name():
    """Test name validation."""
    assert validate_name("Syed Abdul Wahab") is True
    assert validate_name("") is False
    assert validate_name("   ") is False
