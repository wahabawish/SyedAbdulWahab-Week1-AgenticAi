def valiudate_marks(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return False
    return True