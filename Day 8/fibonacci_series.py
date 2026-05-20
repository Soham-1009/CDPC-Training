def fibonacci(x):
    if x==0:
        return 0
    if x==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
if __name__=="__main__":
    x=10
    for x in range(x):
        print(fibonacci(x),end="")