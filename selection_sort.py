# Ascending order

def sel_sort(arr):
    for i in range(len(arr) - 1):
        min = arr[i]
        loc=i
        for j in range(i+1,len(arr)):
            if min > arr[j]:
                min = arr[j]
                loc = j
        arr[i], arr[loc] = arr[loc], arr[i]


if __name__ == "__main__":
    arr = [6, 23, 10, 2, 25, 9, 3, 4]
    sel_sort(arr)
    print(*arr)

###########################################################################

# Descending order

def sel_sort(arr):
    for i in range(len(arr) - 1):
        min = arr[i]
        loc=i
        for j in range(i+1,len(arr)):
            if min < arr[j]:
                min = arr[j]
                loc = j
        arr[i], arr[loc] = arr[loc], arr[i]


if __name__ == "__main__":
    arr = [6, 23, 10, 2, 25, 9, 3, 4]
    sel_sort(arr)
    print(*arr)