def modify_string(s):
    new_str = s
    new_str += " World"
    return new_str

original = "Hello"
result = modify_string(original)

print("Original:", original)
print("Returned:", result)