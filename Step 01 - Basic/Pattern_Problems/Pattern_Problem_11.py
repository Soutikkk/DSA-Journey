# Pattern:
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

n = 5

for i in range(n):
    num = 1 if i % 2 == 0 else 0
    
    for j in range(i + 1):
        print(num, end=" ")
        num = 1 - num   # flip between 0 and 1
    print()