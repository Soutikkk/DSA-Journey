# Two Sum Using Hashing (Python)

# Find two numbers whose sum = target.

nums = [2,7,11,15]
target = 9

hashmap = {}

for i, num in enumerate(nums):

    complement = target - num

    if complement in hashmap:
        print(hashmap[complement], i)

    hashmap[num] = i