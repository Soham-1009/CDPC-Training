arr = [1, 2, 3, 4, 5, 6]
key = 22
loc = 3
arr.append(0)
print(arr)
for i in range(len(arr) - 1, loc, -1):
    arr[i] = arr[i-1]
arr[loc]=key
print(arr)