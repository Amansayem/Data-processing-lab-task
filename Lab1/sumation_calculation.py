num1 = float(input("First number: "))
num2 = float(input("Second number: "))

total = num1 + num2
minus = num1 - num2
times = num1 * num2

print("Addition =", total)
print("Subtraction =", minus)
print("Multiplication =", times)

if num2 != 0:
    division = num1 / num2
    print("Division =", division)
else:
    print("Division is not possible.")
