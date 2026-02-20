# What is STL in C++?

# STL = Standard Template Library

# It gives:

# Containers (data structures)

# Algorithms (like sort, binary search)

# Built-in optimized functions

# Python already has most of this built-in 😎

# Python Equivalent of C++ STL

# Let’s go container by container.

# ---------------------------------------------------------------------------

# 1️⃣ Vector (C++)

# C++:

# vector<int> v;

# Python equivalent:

# arr = []

# Python list = dynamic array (like vector)

# Common operations:
# arr.append(10)      # push_back
# arr.pop()           # pop_back
# arr.sort()          # sort
# len(arr)            # size

# Time Complexity:

# Append → O(1)

# Access → O(1)

# Insert middle → O(n)

# -------------------------------------------------------------------------

# 2️⃣ Set (C++ set / unordered_set)

# C++:

# set<int> s;
# unordered_set<int> us;

# Python equivalent:

# s = set()
# Example:
# s.add(10)
# s.add(20)
# print(10 in s)  # True

# Time Complexity:

# Insert → O(1)

# Search → O(1)

# ⚠ Python set is like unordered_set (hash-based)

# If you want sorted:

# sorted(s)


# --------------------------------------------------------------------------


# 3️⃣ Multiset (C++)

# Allows duplicates.

# Python equivalent:

# from collections import Counter

# c = Counter([1,1,2,3])
# print(c)

# Counter behaves like multiset.

# ------------------------------------------------------------------------

# 4️⃣ Map / Unordered Map (C++)

# C++:

# map<int,int>
# unordered_map<int,int>

# Python equivalent:

# d = {}

# Example:

# d["a"] = 10
# print(d["a"])

# Time Complexity:

# Insert → O(1)

# Search → O(1)

# Python dict = unordered_map

# Sorted map equivalent:

# for key in sorted(d):
#     print(key, d[key])

# ------------------------------------------------------------------------


# 5️⃣ Queue

# C++:

# queue<int>

# Python:

# from collections import deque

# q = deque()
# q.append(10)      # push
# q.popleft()       # pop

# Time Complexity:

# O(1)
# ------------------------------------------------------------------------


# 6️⃣ Stack

# C++:

# stack<int>

# Python:

# stack = []
# stack.append(10)   # push
# stack.pop()        # pop

# List works as stack.

# ------------------------------------------------------------------------

# 7️⃣ Deque

# C++:

# deque<int>

# Python:

# from collections import deque
# dq = deque()

# dq.append(10)
# dq.appendleft(20)
# dq.pop()
# dq.popleft()

# All O(1)

# ------------------------------------------------------------------------



# 8️⃣ Priority Queue (Heap)

# C++:

# priority_queue<int>

# Python:

# import heapq

# heap = []
# heapq.heappush(heap, 5)
# heapq.heappush(heap, 2)

# print(heapq.heappop(heap))  # smallest element

# ⚠ Python heap = Min heap by default

# For max heap:

# heapq.heappush(heap, -value)



# ------------------------------------------------------------------------


# 9️⃣ List (C++ STL list)

# C++ doubly linked list.

# Python equivalent:

# from collections import deque

# Python doesn’t directly expose linked list like C++.

# -----------------------------------------------------------------------


# 🔟 Algorithms

# Now important STL algorithms → Python equivalent

# 🔹 sort()

# C++:

# sort(v.begin(), v.end());

# Python:

# arr.sort()
# # OR
# sorted(arr)

# Time Complexity:

# O(n log n)
# 🔹 next_permutation()

# C++:

# next_permutation(v.begin(), v.end());

# Python:

# from itertools import permutations

# list(permutations(arr))
# 🔹 __builtin_popcount()

# Counts number of set bits.

# C++:

# __builtin_popcount(n);

# Python:

# bin(n).count("1")

# Or (faster):

# n.bit_count()
# 🔹 min_element / max_element

# C++:

# *min_element(v.begin(), v.end());

# Python:

# min(arr)
# max(arr)





# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

# | C++ STL        | Python Equivalent |
# | -------------- | ----------------- |
# | vector         | list              |
# | set            | set               |
# | unordered_set  | set               |
# | multiset       | Counter           |
# | map            | dict              |
# | unordered_map  | dict              |
# | queue          | deque             |
# | stack          | list              |
# | priority_queue | heapq             |
# | sort()         | sort()            |
# | popcount       | bit_count()       |