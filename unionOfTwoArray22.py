def unionOfTwoArray(arr1, arr2):
    if len(arr1) > 0 or len(arr2):
        arr1 = arr1 + arr2
        arr1 = set(arr1)
    return " ".join(str(ele) for ele in arr1)
if __name__ == "__main__":
    arr1 = [1, 2, 4, 5, 6]
    arr2 = [2, 3, 5, 7]
    print(unionOfTwoArray(arr1, arr2))
