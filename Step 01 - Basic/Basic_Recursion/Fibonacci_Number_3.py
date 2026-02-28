# Better Approach 

# 👉 No array needed
# 👉 Only two variables used
# 👉 Space optimized

n = int(input("Enter N: "))

if n == 0:
    print(0)
else:
    second_last = 0
    last = 1

    print(second_last, end=" ")
    if n >= 1:
        print(last, end=" ")

    for i in range(2, n + 1):
        current = second_last + last
        print(current, end=" ")
        second_last = last
        last = current


# 🔹 Time Complexity: O(N)
# 🔹 Space Complexity: O(1) ✅ (Best)