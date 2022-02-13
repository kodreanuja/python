def kthDistictString(arr, k):
    count = 0
    for i in range(len(arr)):
        j = 0
        while(j <len(arr)):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        if(j == len(arr)):
            count += 1

        if (count == k):
            return arr[i]        

    return  -1
arr = ["d", "b", "c", "b","c", "a"]
k = int(input())
print(kthDistictString(arr, k))