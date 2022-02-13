def reachToTheEnd(arr, l, h):
    if l == h:
        return 0
    if arr[l] == 0:
        return float("inf")

    min = float("inf")

    for i in range(l+1, h+1):
        if i < l + arr[l] + 1:
            jumps = reachToTheEnd(arr, i, h)  
            if jumps != float("inf") and jumps + 1 < min:
                min = jumps + 1


    return min               


if __name__ == "__main__":
    # arr = [1, 3, 4, 5, 2]
    arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
    print(reachToTheEnd(arr, 0, len(arr)))       
    
