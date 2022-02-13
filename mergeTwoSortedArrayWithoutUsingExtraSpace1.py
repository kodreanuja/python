def merge(arr1, arr2):

    for i in range(len(arr1)):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            j = 0
            while j + 1< len(arr2) and arr2[j] > arr2[j+1]:
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
                j += 1

    return arr1 + arr2    


if __name__ == "__main__":
    arr1 = [1, 2, 4, 6]
    arr2 = [ 3, 5, 7]
    print(merge(arr1, arr2))
