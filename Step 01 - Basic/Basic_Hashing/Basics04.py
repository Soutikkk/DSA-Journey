# Simple Hash Table using list

hash_table = [None] * 10   # create hash table of size 10

def hash_function(key):
    return key % 10        # simple hash function

def insert(key):
    index = hash_function(key)
    hash_table[index] = key

def search(key):
    index = hash_function(key)
    if hash_table[index] == key:
        print("Key found at index", index)
    else:
        print("Key not found")

# inserting values
insert(15)
insert(25)
insert(35)

print("Hash Table:", hash_table)

# searching
search(25)
search(20)