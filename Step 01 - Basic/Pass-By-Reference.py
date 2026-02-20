def modify(lst):
    lst.append(10)
    print("Inside function:", lst)

nums = [5]
modify(nums)
print("Outside function:", nums)