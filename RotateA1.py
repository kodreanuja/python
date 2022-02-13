def revserse(arr, s, e):
    while s < e:
        temp = arr[s]
        arr[s] = arr[e]
        arr[e] = temp 
        s += 1
        e -= 1
         
def rotate(arr,d):
    if d == 0:
        return 
    n = len(arr)  
    d = d % n  
    revserse(arr, 0, d -1)
    revserse(arr, d, n-1)
    revserse(arr, 0, n-1) 
    return arr

  
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 8]
    d = 2
    print(rotate(arr,d))
   