
n = int(input("Enter number of elements: "))


arr = list(map(int, input("Enter elements separated by space: ").split()))

# Create new array
rev = [0] * n

# Fill new array in reverse order
for i in range(n):
    rev[i] = arr[n - 1 - i]

print("Reversed array:", rev)