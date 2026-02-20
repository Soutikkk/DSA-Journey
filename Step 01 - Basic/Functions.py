def modify(lst):
    lst = [100, 200]

nums = [1, 2]
modify(nums)
print(nums)



# | Type   | Mutable? | Changes Reflect? |
# | ------ | -------- | ---------------- |
# | int    | ❌ No     | ❌ No          |
# | float  | ❌ No     | ❌ No          |
# | string | ❌ No     | ❌ No          |
# | list   | ✅ Yes    | ✅ Yes         |
# | dict   | ✅ Yes    | ✅ Yes         |
# | set    | ✅ Yes    | ✅ Yes         |
