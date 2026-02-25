def factorial(X):
    ans = 1
    
    for i in range(1, X + 1):
        ans *= i
        
    return ans

X = 5
result = factorial(X)
print(f"The factorial of {X} is {result}")