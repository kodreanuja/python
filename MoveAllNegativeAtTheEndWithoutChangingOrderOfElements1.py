def moveAllNeg(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr        
if __name__ == "__main__":
    arr =  [1 ,-1 ,-3 , -2, 7, 5, 11, 6 ]
    print(moveAllNeg(arr))