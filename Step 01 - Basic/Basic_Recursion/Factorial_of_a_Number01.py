
X = int(input("Enter a number: "))

# Start with 1
fact = 1

# Multiply numbers from 1 to X
for i in range(1, X + 1):
    fact = fact * i


print("Factorial of", X, "is", fact)