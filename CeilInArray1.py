def ceilOf(arr, n):
    temp = []
    for i in range(len(arr)):
        if arr[i]>= n:
            temp.append(arr[i])
    return min(temp)        


if __name__ == "__main__":
    arr = [12, 3, 4, 15, 19, 90]
    n = 15
    print(ceilOf(arr, n))