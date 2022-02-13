def rotationArray(arr):
    l = len(arr)
    temp = arr[l -1]
    for i in range(l-1, 0,-1 ):
        arr[i] = arr[i-1]
    arr[0] = temp 
    return ' '.join(str(i) for i in arr)
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]    
    print(rotationArray(arr))