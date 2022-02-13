def rearrangeArray(arr, n) :
    arr.sort()
    temp = [0] * (n + 1)

    Index = 0

    i = 0
    j = n-1
    
    while(i <= n // 2 or j > n // 2 ) :
    
        temp[Index] = arr[i]
        Index = Index + 1
        temp[Index] = arr[j]
        Index = Index + 1
        i = i + 1
        j = j - 1
    
    for i in range(0, n) :
        arr[i] = temp[i]
        
if __name__ == "__main__":
   arr = [ 5, 8, 1, 4, 2, 9, 3, 7, 6 ]
   n = len(arr)
   print(rearrangeArray(arr, n))

   for i in range(0, n) :
       print( arr[i], end = " ")
    