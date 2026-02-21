x = int(input("Enter a number : "))

string_x = str(x)
reversed_x = string_x[::-1]

if string_x == reversed_x:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")