arr1=[1,2,2,3]
arr2=[2,2]
arr3=[]
for i in arr1:
    for j in arr2:
        if i==j:
            if i not in arr3:
                arr3.append(i)
print(arr3)
    