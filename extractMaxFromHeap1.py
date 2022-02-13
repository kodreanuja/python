def extractMax(arr):
    n = len(arr)
    if len(arr) < 1:
        return "UnderFlow."
    max1 = arr[0]
    arr[0] = arr[len(arr) -1]    
    n -= 1
    maxHeap(arr, 0)
    return max1
     
def maxHeap(arr, i):
    l = 2 * i + 1
    r = 2 * i + 2
    for i in range(len(arr)):
        if (l < len(arr) and arr[l] > arr[i]):
            largest = l

        else:
            largest = i
            if (r < len(arr) and arr[r] > arr[largest]):
               largest = r
        if (largest != i):
            arr[i], arr[largest] = arr[largest] , arr[i]
            maxHeap(arr, i)    
           

if __name__ == "__main__":
    arr = [9,8,7,6,5,4,3]
    i = 0
    print(extractMax(arr))
 