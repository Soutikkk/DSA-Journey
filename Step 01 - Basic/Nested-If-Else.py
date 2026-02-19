age = int(input("Enter your age : "))
has_IDcard = True

if age >= 18:
    if has_IDcard:
        print("You can enter.")
    else:
        print("You need ID.")
else:
    print("You are too young.")