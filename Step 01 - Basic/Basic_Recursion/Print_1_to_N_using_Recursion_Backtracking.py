def print_numbers(current, n):
    if current > n:
        return
    
    print_numbers(current + 1, n)
    print(current, end=" ")


# Call function
print_numbers(1, 4)