no=int(input("Enter the number:"))
rev=0
save=no
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
if rev==save:
    print("no is pallindrome")
else :
    print("no is not a pallindrome")