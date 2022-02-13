def arrayRotation(arr):
    l = len(arr)
    i = 0
    j = l -1
    if l <= 1:
        return "no rotation posible."
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i +=1
    return " ".join(str(ele) for ele in arr)   
    
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    print(arrayRotation(arr))  