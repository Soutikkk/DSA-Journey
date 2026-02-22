def print_numbers(n):
    if n == 0:      # Base case (stop)
        return
    
    print(n)        # Print first
    print_numbers(n-1)   # Then call for smaller number


print_numbers(4)