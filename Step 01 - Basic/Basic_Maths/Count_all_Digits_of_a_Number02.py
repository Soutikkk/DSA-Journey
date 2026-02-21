def countDigits(n):
    # Handle the case where n is 0, as the loop won't run
    if n == 0: return 1
    
    # Use absolute value to handle negative numbers
    n = abs(n)
    cnt = 0
    
    while n > 0:
        cnt = cnt + 1
        n = n // 10  # Integer division to drop the last digit
        
    # Return is now OUTSIDE the loop
    return cnt

if __name__ == "__main__":
    N = int(input("Enter a number N : "))
    digits = countDigits(N)
    print("Number of Digits in N:", digits)