# Pattern:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n = 5

# Increasing
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# Decreasing
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()