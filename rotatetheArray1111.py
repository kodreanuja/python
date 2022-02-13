def arrRotate(arr):
    for i in range(0,n):
        temp = arr[0]
        for j in range(0, len(arr)-1):
            arr[j] = arr[j +1]
        arr[len(arr) -1] = temp 

def printArray(arr):
    for i in range(0,len(arr)):
        print("%d"%arr[i], end =" ") 

       

if __name__ == "_main__":
    arr = [1, 3, 4, 5, 6]
    n = 1
    print(arrRotate(arr))
    print(printArray(arr))
    
