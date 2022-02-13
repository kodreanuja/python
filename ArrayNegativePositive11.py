def arrangeArray(array):
    l = len(array)
    j = 0
    for i in range(0, l):
        if array[i] < 0:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            j = j + 1
    return array
    # return array.sort()  
if __name__ == "__main__":
    N = int(input()) 
    array = list(map(int, input().split()))  
    print(arrangeArray(array)) 
