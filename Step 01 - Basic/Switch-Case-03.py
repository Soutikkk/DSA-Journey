
# Define a character variable representing a grade
grade = 'B'

# Evaluate grade using match-case (Python 3.10+)
match grade:
    case 'A':  # If grade is 'A'
        print("Excellent!")
    case 'B':  # If grade is 'B'
        print("Good!")
    case _:    # Default case (no match)
        print("Not specified.")

