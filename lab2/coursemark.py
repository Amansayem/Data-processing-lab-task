
marks = [85, 72, 91, 48, 67]   


total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)
passed = sum(1 for m in marks if m >= 50)

print("Marks:", marks)
print("Total Marks:", total)
print("Average Mark:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Courses Passed:", passed)
