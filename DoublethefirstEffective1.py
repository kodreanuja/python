def pushZerosToEnd(arr, n):
    lasti = 0
    for i in range(0, n):
        if arr[i] != 0:
            arr[i], arr[lasti] = arr[lasti], arr[i]
            lasti += 1


def x(arr):
    if len(arr) == 1:
        return 
    for i in range(0, len(arr)-1):
        if (arr[i] != 0) and (arr[i] == arr[i+1]):
            arr[i] = 2 * arr[i]  
            arr[i + 1] = 0
            i += 1

    pushZerosToEnd(arr, n)  
    return arr      
     
   

if __name__ == "__main__":
    arr = [0,2, 2, 2, 0, 6, 6, 0, 0 ,8]
    n = len(arr)
    print(x(arr))