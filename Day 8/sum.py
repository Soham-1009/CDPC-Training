def natural(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else :
        return n + natural(n-1)

if __name__ == "__main__":
    n=1
    print("Sum is:", natural(n))