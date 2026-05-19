# n1=10
# n2=20
# n3=30
# max = n1
# if max<n2:
#     max=n2
# if max<n3:
#     max=n3
# print (max)

# n=int(input("Enter the no: "))
# if n%2==0:
#     print("no is even")
# else:
#     print("no is odd")

#############################################################

# per=75
# if per>=40 and per<=60:
#     print ("take admission in ABC College ")
# elif per>=61 and per<=80:
#     print ("take admission in XYZ College ")
# elif per>=81 and per<=100:
#     print ("take admission in PQR College ")

##################################################################
cp = int(input("Enter the cost price"))
st = input("Are you a student y/n")
if st == "y":
    if cp > 500:
        ds = cp * 10
    else:
        ds = cp * 8
else:
    if cp > 500:
        ds = cp * 8
    else:
        ds = cp * 2
net = cp - ds
