class Solution:
    # Function to find sum of first N natural numbers using formula
    def sumOfNaturalNumbers(self, N):
        # Apply formula directly
        return (N * (N + 1)) // 2

# Driver code
if __name__ == "__main__":
    obj = Solution()
    N = int(input())
    print(obj.sumOfNaturalNumbers(N))
