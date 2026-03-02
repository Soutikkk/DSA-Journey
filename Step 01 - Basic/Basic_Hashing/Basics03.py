from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

freq = Counter(arr)

q = int(input())
for _ in range(q):
    number = int(input())
    print(freq[number])