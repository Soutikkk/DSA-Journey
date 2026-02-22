def print_numbers(n):
    if n == 0:      # Base case (stop)
        return
    
    print_numbers(n-1)   # First go down
    print(n)             # Then print


print_numbers(4)