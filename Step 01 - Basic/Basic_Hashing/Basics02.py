# Number Hashing using list

n = int(input())
arr = list(map(int, input().split()))

# Assuming maximum element <= 12
hash_array = [0] * 13   # size = max_element + 1

# Precompute (Pre-storing)
for num in arr:
    hash_array[num] += 1

q = int(input())
for _ in range(q):
    number = int(input())
    print(hash_array[number])   # Fetching


#     ⏱ Time Complexity:

# Precompute → O(N)

# Each Query → O(1)

# Total → O(N + Q)