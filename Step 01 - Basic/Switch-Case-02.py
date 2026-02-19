
# Define two constant integers
x = 10
y = 5

# Evaluate the sum of x and y using match-case 

match x + y:
    case 15:  # If the sum equals 15
        print("Result is 15.")
    case 20:  # If the sum equals 20
        print("Result is 20.")
    case _:   # Default case (no match)
        print("No match found.")

