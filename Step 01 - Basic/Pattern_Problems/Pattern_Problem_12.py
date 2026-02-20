# Pattern:
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n = 5

for i in range(1, n + 1):
    
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end="")
    
    # Decreasing numbers
    for j in range(i, 0, -1):
        print(j, end="")
    
    print()