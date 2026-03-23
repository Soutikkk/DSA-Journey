arr = list(map(int, input("Enter elements: ").split()))

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)