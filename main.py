def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
student_name = input("Enter the student name: ")
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))

grades_list = [grade1, grade2, grade3, grade4, grade5]
average_score = sum(grades_list) / len(grades_list)

letter_grade = get_letter_grade(average_score)

print(f"Student Name: {student_name}")
print(f"Average: {average_score:.1f}")
print(f"Letter Grade: {letter_grade}")

