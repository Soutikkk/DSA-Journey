# What is a Divisor?

# A number d is called a divisor of N if:
# N%d=0
# That means it divides N without remainder.
# Example 1: N = 36
# Divisors:
# 1, 2, 3, 4, 6, 9, 12, 18, 36

class Solution:
    def getDivisors(self, N):
        res = []
        
        for i in range(1, N + 1):
            if N % i == 0:
                res.append(i)
        
        return res


# Example
sol = Solution()
print(sol.getDivisors(36))