# s="My name is Soham Deshpande"
# print(s.find("Soham"))
# print(s.rfind('e'))

# r='abababacccadda'
# print(r.count('a'))
# print(r.count('b'))

# t="My name is Sohan Deshpande"
# t1=t.replace("Sohan","Soham")
# print(t1)

# b="My name is Sohan Deshpande"
# ls=b.split()
# print(ls)

# a="www.soham.com"
# ls=a.split(".")
# print(ls)

# c=["Nagpur", "Pune", "Mumbai", "Sangli"]
# ls=' '.join(c)
# print(c)

# d=input("Enter the string:")
# print(d[::-1])

# e=input("Enter the string:")
# print(':'.join(reversed(e)))

# f="Learning python is very easy"
# ls=f.split(" ")
# ls=ls[::-1]

# print(f.join(reversed(ls)))

# g="Learning python is very easy"
# ls=g.split()
# print(' '.join(reversed(ls)))

# h="abababacccadda"
# ans=""
# for i in h:
#     if i not in ans:
#         ans=ans+i
# print (ans)

# no=input("Enter the mobile no.: ")
# if no.isdigit():
#     if len(no)==10 :
#         if no[0] in ['6','7','8','9']:
#             print("Valid no.")
#         else:
#             print("Invalid no. in India.")
#     else:
#         print("Invalid no.(should be of length 10).")
# else:
#     print("Invalid no. (should contain only numbers).")


rec={}
n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Enter the name: ")
    marks=float(input("Enter the marks: "))
    rec[name]=marks

print (rec)
for x in rec:
    print (x,"\t",rec[x])