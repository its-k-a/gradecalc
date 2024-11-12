def calculate_average(*grades):
    total_grades = len(grades)
    result = 0
    for grades in grades:
     result += grades

    return result / total_grades

# Test cases
print(calculate_average(85, 90, 78, 92))
print(calculate_average(100, 95))