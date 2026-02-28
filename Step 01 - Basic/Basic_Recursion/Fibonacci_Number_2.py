# Brute Force (Using Array)



n = int(input("Enter N: "))

if n == 0:
    print(0)
elif n == 1:
    print("0 1")
else:
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    for num in fib:
        print(num, end=" ")



# 🔹 Time Complexity: O(N)
# 🔹 Space Complexity: O(N)