def reArrange(arr, n):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    pos, neg = i + 1 , 0
    while pos < n and neg < n and  arr[neg] < 0:
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2

    return arr    



if __name__ == "__main__":
    arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    n = len(arr)
    print("Given Array is:")
    print(arr)
    print(reArrange(arr, n))



