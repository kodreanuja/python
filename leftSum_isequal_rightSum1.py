arr = list(map(int, input().split()))
print(arr)
n = len(arr)
def find(arr, n):
    leftSum =0
    rightSum =0
    for i in range(1,n):
        rightSum += arr[i]
    i =0
    j = 1
    while j < n:
        rightSum -= arr[j]
        leftSum += arr[i]
        if leftSum == rightSum:
            return arr[i+1]
        i+=1
        j+=1
    return -1     
if __name__=="__main__":
    print(find(arr, n))