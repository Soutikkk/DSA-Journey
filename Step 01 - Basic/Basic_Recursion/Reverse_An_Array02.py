# Take number of elements
n = int(input("Enter number of elements: "))

# Take array input
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Two pointer method
p1 = 0
p2 = n - 1

while p1 < p2:
    arr[p1], arr[p2] = arr[p2], arr[p1]
    p1 += 1
    p2 -= 1

print("Reversed array:", arr)