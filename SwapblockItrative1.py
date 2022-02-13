def leftRotate(arr, d, n):
    if(d == 0 or d == n):
        return
    i = d
    j = n - d
    while (i != j):
         
        if(i < j): 
            swap(arr, d - i, d + j - i, i)
            j -= i
         
        else: 
            swap(arr, d - i, d, j)
            i -= j
     
    swap(arr, d - i, d, i)


def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ")
    print()

def swap(arr, fi, si, d):
    for i in range(d):
        temp = arr[fi + i]
        arr[fi + i] = arr[si + i]
        arr[si + i] = temp;    


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = int(input())
    n = len(arr)
    leftRotate(arr, 2, 7)
    printArray(arr, 7)
