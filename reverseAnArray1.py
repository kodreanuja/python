def reverseAnArray(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr    

if __name__ == "__main__":
    arr = [3, 4, 6]
    print(reverseAnArray(arr))