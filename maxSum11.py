def maxSum(array):
    l = len(array)
    sum = 0
    for i in range(0,l):
        sum = sum + array[i]
    if sum < 0:
        sum = array[0]
        return sum
    else:
        return sum    


if __name__ == "__main__":
    N = int(input())
    array = list(map(int, input().split()))
    print(maxSum(array))    