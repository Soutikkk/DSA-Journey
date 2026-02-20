n = int(input("Enter a number: "))
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print("Factorial is:", factorial)


# | For Loop                       | While Loop                       |
# | ------------------------------ | -------------------------------- |
# | Used when iterations are known | Used when condition-based        |
# | Cleaner for counting           | Flexible for conditions          |
# | Example: 1 to 10               | Example: run until user enters 0 |
