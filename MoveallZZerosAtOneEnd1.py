def pushZerosInArray(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1  

    return arr    

               

if __name__ == "__main__":
    arr = [0, 1, 3, 0, 5, 0, 7, 0, 9]
    print(pushZerosInArray(arr))