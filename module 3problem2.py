print("Enter student last name:")
last_name = input()

print("Enter midterm exam score:")
midterm = float(input())

print("Enter final exam score:")
final_exam = float(input())

total_exam_points = (midterm * 0.40) + (final_exam * 0.60)

print("Student Last Name:", last_name)
print("Total Exam Points:", format(total_exam_points, ".2f"))
