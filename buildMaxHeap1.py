def BuildHeap(arr):
    l = len(arr)
    for i in range((l//2 )-1, 0):
        BuildHeap(arr, i)

    return arr    

if __name__ == "__main__":
    arr = [2, 3, 4]
    print(BuildHeap(arr))