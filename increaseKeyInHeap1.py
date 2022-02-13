def increaseKey(arr, i, key):
    if key < arr[i]:
        return "Wrong operation"
    arr[i] = key 
    while (i > 0 and arr[i//2] < arr[i]):
        arr[i], arr[i//2] = arr[i//2], arr[i]
        i = i//2     
    return arr
 
if __name__ == "__main__":
    arr = [9,8,7,6,5,4,3]
    i = 3
    key = 15
    print(increaseKey(arr, i, key))
 