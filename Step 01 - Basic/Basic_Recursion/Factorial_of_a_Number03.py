def factorial(n):
    if n == 0:   # Base Case
        return 1
    
    return n * factorial(n - 1)

n = 3
print(factorial(n))




# | Feature | Iterative       | Recursive                        |
# | ------- | --------------- | -------------------------------- |
# | Uses    | Loop            | Function calls itself            |
# | Space   | O(1)            | O(N)                             |
# | Speed   | Slightly faster | Slightly slower (stack overhead) |
# | Memory  | Less            | More                             |