# Pattern:
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

n = 5

for i in range(n):
    
    # Spaces
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Increasing alphabets
    for j in range(i + 1):
        print(chr(65 + j), end="")
    
    # Decreasing alphabets
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    
    print()