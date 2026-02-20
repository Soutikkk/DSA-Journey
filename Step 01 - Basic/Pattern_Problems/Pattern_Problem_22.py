# Pattern: Number Square


# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4


n = 4
size = 2 * n - 1

for i in range(size):
    for j in range(size):
        
        top = i
        bottom = j
        right = size - 1 - j
        left = size - 1 - i
        
        print(n - min(min(top, bottom), min(left, right)), end=" ")
    
    print()