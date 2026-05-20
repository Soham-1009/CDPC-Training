n = 5

def fact(n=1):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

if __name__ == "__main__":
    ans = fact
    print("factorial is", fact(n))
