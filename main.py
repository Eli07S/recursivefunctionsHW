# Eli.SK
# Recursive function HW
# 19 October 2023

# First recursive function
# This function finds the factorial of number "x"
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 8
print("The factorial of", num, "is", factorial(num))

# Second recursive function
# This function counts down from "x" and ends at 0
def countdown(x):
    print(x)
    if x == 0:
        return
    else:
        countdown(x - 1)
countdown(22)