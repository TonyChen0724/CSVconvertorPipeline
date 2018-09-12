str = "123***456"
arr = str.split("*")

while '' in arr:
    arr.remove('')

print(arr)