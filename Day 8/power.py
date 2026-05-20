
def power(x,y):
    if x==0 :
        return 0
    elif y==0:
        return 1
    elif y==1:
        return x
    elif x==1:
        return 1
    else: 
        return x*power(x,y-1)

if __name__ == "__main__":
    x=2
    y=3
    print("Power is:", power(x,y))