n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

arr = arr[::-1]

print("Reversed array:", arr)



# | Method       | Space | Interview Friendly         |
# | ------------ | ----- | -------------------------- |
# | Brute Force  | O(n)  | ❌                         |
# | Two Pointers | O(1)  | ✅ BEST                    |
# | Slicing      | O(n)  | ⚠️ Good but less preferred |
