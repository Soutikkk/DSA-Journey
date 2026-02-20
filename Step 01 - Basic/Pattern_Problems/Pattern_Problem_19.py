# Pattern: Hollow Butterfly

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

n = 5

# Upper Half
for i in range(n):
    
    # Stars
    for j in range(n - i):
        print("*", end="")
    
    # Spaces
    for j in range(2 * i):
        print(" ", end="")
    
    # Stars
    for j in range(n - i):
        print("*", end="")
    
    print()

# Lower Half
for i in range(n):
    
    # Stars
    for j in range(i + 1):
        print("*", end="")
    
    # Spaces
    for j in range(2 * (n - i - 1)):
        print(" ", end="")
    
    # Stars
    for j in range(i + 1):
        print("*", end="")
    
    print()