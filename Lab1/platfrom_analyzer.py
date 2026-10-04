student_name = input("Enter your name: ")

marks = []
passed_courses = 0

for course in range(5):
    mark = float(input("Enter marks for course " + str(course + 1) + ": "))
    marks.append(mark)

    if mark >= 50:
        passed_courses += 1

total = sum(marks)
average = total / len(marks)

highest = max(marks)
lowest = min(marks)

if average >= 80:
    performance = "Excellent"
elif average >= 70:
    performance = "Good"
elif average >= 60:
    performance = "Satisfactory"
elif average >= 50:
    performance = "Pass"
else:
    performance = "Needs Improvement"

print("\nName:", student_name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Number of Passed Courses:", passed_courses)
print("Result:", performance)
