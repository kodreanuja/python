def leftRotateArrayByDElemnents(arr, d):
    for i in range(d):
        leftRotateArrayOneByOne(arr, l)
    return arr    

def  leftRotateArrayOneByOne(arr, l):
    temp = arr[0]
    for i in range(l-1):
        arr[i] = arr[i+1]
    arr[l-1] = temp    

if __name__ == "__main__":
    arr = [1, 3, 5, 6, 7, 2]
    d = 2 
    l = len(arr)
    print(leftRotateArrayByDElemnents(arr, d))