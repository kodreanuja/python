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
    return  arr             



if __name__ == "__main__":
    arr = [2, 3, 4]
    i = int(input()) 
    print(maxHeap(arr, i))
