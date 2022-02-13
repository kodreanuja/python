def merge(arr1, m, arr2,  n) -> None:
        last = m + n -1
        while m > 0 and n > 0 :
            if arr1[m - 1] > arr2[n - 1]:
                arr1[last] = arr1[m - 1]
                m -= 1
            else:
                arr1[last] = arr2[n - 1] 
                n -= 1  
            last -= 1

        while n > 0 :
            arr1[last] = arr2[n - 1]  
            n -= 1
            last -= 1  
        return arr1  
if __name__ =="__main__":
    arr1 = [1,2,3,0,0,0]
    m = 3
    arr2 = [2, 5, 6]
    n = 3 
    print(merge(arr1, m, arr2, n))
