def nextGreaterElement(arr):
    if len(arr) == 0:
        return 

    for i in range(len(arr)):
        NGE = -1
        for j in range(i +1, len(arr)):
            if arr[j] > arr[i]:
                NGE = arr[j]  
                break  
        print(NGE, end = " ")



if __name__ == "__main__":
    arr = [13, 7, 6, 12, 10]
    print(nextGreaterElement(arr))