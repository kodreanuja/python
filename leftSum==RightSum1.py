def findElement(arr, n) :
    prefixSum = [0] * n
    prefixSum[0] = arr[0]
    for i in range(1, n) :
        prefixSum[i] = prefixSum[i - 1] + arr[i]

    suffixSum = [0] * n
    suffixSum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1) :
        suffixSum[i] = suffixSum[i + 1] + arr[i]

    for i in range(1, n - 1, 1) :
        if prefixSum[i] == suffixSum[i] :
            return arr[i]
         
    return -1
 
if __name__ == "__main__" :
     
    arr = [ 1, 4, 2, 5]
    n = len(arr)
    print(findElement(arr, n))