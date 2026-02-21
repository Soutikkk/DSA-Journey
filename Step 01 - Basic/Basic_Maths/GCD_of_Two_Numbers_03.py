def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example
print(find_gcd(20, 15))