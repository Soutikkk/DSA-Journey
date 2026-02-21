

x = int(input("Enter a number : "))

reverse = 0

while x > 0:
    remainder = x % 10
    reverse = (reverse * 10) + remainder
    x = x // 10

print("Reverse of the number is : ", reverse)