def decreaseKey(arr, i, key):
    if arr[i] < key:
        return "Wrong Operation."
    
    arr[i] = key 
    maxHeap(arr, i)

    return arr

def maxHeap(arr, i):
    l = i * 2 + 1
    r = i * 2 + 2
    for i in range(len(arr)):
        if l < len(arr) and arr[l] > arr[i]:
            largest = l

        else:
            largest = i
            if r < len(arr) and arr[r] > arr[largest]:
                largest = r

        if largest != i:
            arr[i], arr[largest] =  arr[largest], arr[i] 
            maxHeap(arr, i) 

    return arr        


if __name__ == "__main__":
    arr = [9,8,7,6,5,4,3]
    i = 1
    key = 2
    print(decreaseKey(arr, i, key)) 