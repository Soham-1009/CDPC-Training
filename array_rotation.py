arr = [1, 2, 3, 4, 5]
k = 2
print(arr)
for i in range(k):
    temp = arr [- 1]
    for j in range(len(arr) - 1,0,-1):
        arr[j] = arr[j - 1]
    arr[0]=temp
print(arr)
# for i in range(loc +1,len(arr)):
#     arr[i-1] = arr[i]
# arr.pop()
# print(arr)
