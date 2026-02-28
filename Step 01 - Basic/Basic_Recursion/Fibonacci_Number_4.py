# 3️Recursive Approach 



def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter N: "))
print(fibonacci(n))


# 🔹 Time Complexity: O(2^N) ❌ (Very Slow)
# 🔹 Space Complexity: O(N)