# Simple Python Program to Demonstrate Input and Output

# Taking single input
x = int(input("Enter a number: "))

# Taking multiple inputs
a, b = map(int, input("Enter two numbers separated by space: ").split())

# Printing output
print("\n--- Output Section ---")
print("Value of x:", x)
print("Value of a:", a)
print("Value of b:", b)

# Showing use of newline character
print("\nSum of a and b is:", a + b)