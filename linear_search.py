def linear_search(n, arr, target):
    flag = False
    loc = -1
    for i in range(n):
        if arr[i] == target:
            flag = True
            loc = i
            break
            
    if flag:
        print("Search is successful and present at index:", loc)
    else:
        print("Search is unsuccessful.")

if __name__ == "__main__":
    n = int(input("Enter the size of array: "))
    arr = []
    for i in range(n):
        arr.append(int(input("Enter the Elements: ")))
    target = int(input("Enter no which is to be searched: "))
    linear_search(n, arr, target)
