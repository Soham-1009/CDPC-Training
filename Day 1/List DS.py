# ls=[]
#  print(type(ls))

# ls=list()
# ls=[1.2,3,34.546,34]

# arr=[1,2,3,34,546,34]
# print (arr)

# for i in range(len(arr)):
#     print (arr[i], end="")

# for x in arr:
#     print(x,end="")

# arr=[1,2,3,34,546,34]
# max=arr[0]
# min=arr[0]
# for i in range(1,len(arr)):
#     if arr[i]>max:
#         max=arr[i]
#     if arr[i]>min:
#         min=arr[i]
# print (max)
# print (min)

# arr=[1,2,3,34,546,34]
# print (arr[1:5])
# print (arr[:5])
# print (arr[1:])
# print (arr[:])
# print (arr[1::5])

# print(max(arr))
# print(min(arr))

arr=[5,3,9,2,8,4,5,3,3,9]
ans=[]
for x in arr:
    if x not in ans:
        ans.append(x)
print (ans)