
marks = [85, 72, 91, 48, 67]

total = sum(marks)
average = total / len(marks)

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
