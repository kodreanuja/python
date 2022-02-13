def leftRotateArrayByD(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)
        

def leftRotatebyOne(arr, n):
    temp = arr[0] 
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr):
    for i in range(len(arr)):
        return arr


if __name__ == "__main__":
    arr = [1, 3, 5, 6, 7, 2]
    d = 2
    n = len(arr)
    print(leftRotateArrayByD(arr, d, n))
    print(printArray(arr))