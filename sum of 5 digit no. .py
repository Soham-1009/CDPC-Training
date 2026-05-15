no=int(input("Enter the no:"))
n1= no%10
no=no//10
n2=no%10
no=no//10
n3=no%10
no=no//10
n4=no%10
no=no//10
n5=no%10
rev=n1*10000+n2*1000+n3*100+n4*10+n5*1
res=n1+n2+n3+n4+n5
print(res)
print(rev)