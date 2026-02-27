# 2️⃣ Optimal Recursive Approach
# ✅ Algorithm

# Compare first and last characters.

# If not equal → return False.

# If equal → recursively check remaining substring.

# Base case → when index reaches middle.


def palindrome(i, s):

    # Base Case
    if i >= len(s) // 2:
        return True

    if s[i] != s[len(s) - i - 1]:
        return False

    return palindrome(i + 1, s)


# Driver Code
s = input("Enter string: ")

if palindrome(0, s):
    print("Palindrome")
else:
    print("Not Palindrome")




# ⏱ Complexity

# Time Complexity: O(N)

# Space Complexity: O(N) (due to recursion stack)