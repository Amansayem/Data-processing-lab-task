employee_name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))
extra = float(input("Enter allowances: "))

total_salary = salary + extra

if total_salary > 80000:
    rate = 15
elif total_salary > 50000:
    rate = 10
elif total_salary > 30000:
    rate = 5
else:
    rate = 0

tax = total_salary * rate / 100
final_salary = total_salary - tax

print("Employee Name:", employee_name)
print("Total Salary:", total_salary)
print("Tax Rate:", rate, "%")
print("Tax:", tax)
print("Salary After Tax:", final_salary)