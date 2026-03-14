# Advanced Hashing means using hashing techniques to solve problems efficiently (usually in O(1) average time) for searching, counting, grouping, or detecting duplicates. Instead of looping again and again through arrays, we store values in a hash table.

# A hash table stores data in key → value pairs using a hash function to compute the index.

# In Python → implemented using dictionary (dict)
# In C → implemented manually using arrays + hashing logic

# 1️⃣ Basic Idea of Hashing

# Suppose we have numbers:

# [3, 5, 3, 2, 5, 5, 7]

# We want to count frequency of each number.

# Instead of checking repeatedly:

# 3 → 2 times
# 5 → 3 times
# 2 → 1 time
# 7 → 1 time

# We store counts using a hash table.