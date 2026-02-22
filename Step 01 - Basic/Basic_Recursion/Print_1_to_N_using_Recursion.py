def print_numbers(current, n):
    if current > n:   # Base case (stop)
        return
    
    print(current, end=" ")
    print_numbers(current + 1, n)


# Call function
print_numbers(1, 4)