# arr=[1,2,3,4,5,5]
# for i in range(len(arr)):
#     print(arr[i])
# for x in arr:
#     print(x)


# for i in range(1,6):
#     for j in range(10,5,-1):
#         if i == 3 and j==8:
#             continue
# print (i, j )

i=1
j=10
while i<j:
    if i == 3:
        i=i+1
        j=j-1
        continue
    print(i,"\t",j)
    i=i+1
    j=j-1  