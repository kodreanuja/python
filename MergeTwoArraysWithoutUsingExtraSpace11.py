def merge(arr1, arr2, m, n):
    i = 0
    while(i < m):
        arr1[i + m] = arr2[i]
        i += 1
        arr1.sort()
    return arr1    


if __name__ == "__main__":
    arr1 = [1, 5, 9, 10, 15, 20]
    arr2 = [2, 3, 8, 13]
    m = len(arr1)
    n = len(arr2)
    m = m + n
    print(merge(arr1, arr2, m,n))
