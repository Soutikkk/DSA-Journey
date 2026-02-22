class Solution:
    # Function to find sum of first N natural numbers using loop
    def sumOfNaturalNumbers(self, N):
        # Initialize sum to 0
        total = 0
        
        # Loop from 1 to N
        for i in range(1, N + 1):
            # Add current number to sum
            total += i
        
        # Return the computed sum
        return total

# Driver code
if __name__ == "__main__":
    # Create object of Solution class
    obj = Solution()
    
    # Input value for N
    N = int(input())
    
    # Call the function and store the result
    result = obj.sumOfNaturalNumbers(N)
    
    # Print the result
    print(result)
