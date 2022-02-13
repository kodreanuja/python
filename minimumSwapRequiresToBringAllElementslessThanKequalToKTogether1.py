def minimumSwap(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] <= k:
            count += 1

    bad = 0
    for i in range(0, count):
        if arr[i] > k:
            bad += 1

    result = bad 
    j = count 
    for i in range(0, len(arr)):

        if j == len(arr):
            break

        if arr[i] > k:
            bad += 1

        result = min (result, bad)  
        j += 1   

    return result    

if __name__ == "__main__":
    arr = [2, 7, 9, 5, 8, 7, 4] 
    k = int(input())
    print(minimumSwap(arr))              
   
    