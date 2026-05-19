# s=set()
# print(s)
# print(type(s))

#############################################################

# n=int(input("Enter the size:"))
# print("Enter list elements: ")
# arr=[]
# sum=0
# even=0
# odd=0
# e1=0
# o1=0
# for i in range(n):
#     ele=int(input('Enter the Elements: '))
#     arr.append(ele)

# for i in range(len(arr)):
#     if arr[i] %2 ==0:
#         even=even+arr[i]
#         e1=e1+1
#     else:
#         odd=odd+arr[i]
#         o1=o1+1
# print(f"Even sum: {even}, Count: {e1}")
# print(f"Odd sum: {odd}, Count: {o1}")


#############################################################

no=int(input("Enter the no.: "))
save=no
count=0
while no>0:
    no=no//10
    count=count+1
no=save
if count%2==0:
    mid=count//2
    n1=no%10**mid
    n2=no//10**mid
sum=n1+n2
sq=sum**2
if sq==no:
    print ("tech no")
else:
    print("no tech no. ")