import math

def checkPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True


# Example
n = 1483

if checkPrime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")