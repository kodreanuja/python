def missMarbel(arr):
    a = arr[0] 
    b = arr[-1]                #b = arr[len(arr)-1]
    mid = len(arr)//2
    s = a + b
    return s - arr[mid]
if __name__=="__main__":
    arr = [2, 10, 6, 4, 12 ]
    #arr = list(map(int, input().split()))
    print(missMarbel(arr))    