# What is an Armstrong Number ?

# A number is called an Armstrong Number if
# It is equal to the sum of its digits raised to the power of the total number of digits.
# For example, 153 is an Armstrong Number because


def is_armstrong(num):
    k = len(str(num))
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** k
        num //= 10

    return total == original


number = int(input("Enter a number : "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")