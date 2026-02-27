# 1️⃣ Brute Force Approach (Two Pointer Method)
# ✅ Algorithm

# Take two pointers → left = 0 and right = len(s) - 1
# Compare characters from start and end.
# If characters don’t match → Not Palindrome.
# Move pointers towards center.
# If loop completes → Palindrome.


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Driver Code
s = input("Enter string: ")

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")




#     ⏱ Complexity

# Time Complexity: O(N)
# Space Complexity: O(1)