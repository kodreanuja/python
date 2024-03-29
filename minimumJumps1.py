def minjumps(arr, n):
    jumps = [0 for i in range(len(arr))]
    for i in range(n-2, -1, -1):
       
        if (arr[i] == 0):
            jumps[i] = float('inf')

        elif (arr[i] >= n - i - 1):
            jumps[i] = 1

        else:
           
            min = float('inf') 

            for j in range(i + 1, n):
                if (j <= arr[i] + i):
                    if (min > jumps[j]):
                        min = jumps[j]
                        
            if (min != float('inf')):
                jumps[i] = min + 1
            else:
               
                jumps[i] = min 

    return jumps[0]



if __name__ == "__main__":
    arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
    n = len(arr)
    print(minjumps(arr, n))