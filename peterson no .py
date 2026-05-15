n=int(input("Enter the no:"))
save=n
sum=0
fact=1
while n>0:
    rem=n%10
    fact=1
    while n>0:
        fact=fact*rem
        rem=rem-1
    sum=sum+fact
    n=n//10
if save == sum:
    pass