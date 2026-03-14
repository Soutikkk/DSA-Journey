arr = [3,5,3,2,5,5,7]

hashmap = {}

for num in arr:
    if num in hashmap:
        hashmap[num] += 1
    else:
        hashmap[num] = 1

print(hashmap)