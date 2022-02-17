import sys 
def findMin(arr, n):
    if n== 0 or len(arr)==0:
        return 0
    if len(arr) < 2:
        return 
    l = 0
    h = len(arr) - 1
    min = sys.maxsize
    i , j = 0, 0
    while l < h:
        if abs(arr[h]) + abs(arr[l]) < min:
            min = abs(arr[h] + arr[l])
            i, j = l, h

        if min == 0:
            break 

        if arr[h] + arr[l] < 0:
            l = l + 1
        else:
            h = h - 1   

    return arr[h] + arr[l]               


if __name__ == "__main__":
    n = 5 #int(input())
    arr = [13, 16, 15, 17, 18] #list(map(int, input().split()))
    print(findMin(arr, n))