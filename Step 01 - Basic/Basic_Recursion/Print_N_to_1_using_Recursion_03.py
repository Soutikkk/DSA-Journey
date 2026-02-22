class Solution:
    # Recursive function to print numbers from current down to 1 using backtracking
    def printNumbers(self, current):
        # Base case: if current is less than 1, stop recursion
        if current < 1:
            return

        # Recursive call with previous number
        self.printNumbers(current - 1)

        # Print current number during backtracking
        print(current, end=' ')

if __name__ == "__main__":
    sol = Solution()
    n = 10

    sol.printNumbers(n)
    print()
