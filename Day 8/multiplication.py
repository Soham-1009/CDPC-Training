def mul(x,y):
    if y == 1:
        return x
    elif x == 1:
        return y
    elif x==0 or y==0:
        return 0
    else:
        return x+mul(x,y-1)
if __name__ == "__main__":
    x = 2
    y = 3
    print("Multiplication is:", mul(x, y))