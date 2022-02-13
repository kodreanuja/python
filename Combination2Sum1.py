def combinations(arr, target):
    result = []
    arr.sort()
    def findUnique(i, cur, sum1):
        if sum1 == target:
            result.append(cur)
            return 
        elif sum1 > target:
            return 
        else:
            prevSum = -1 
            for j in range(i, len(arr)):
                if arr[j] == prevSum:
                    continue
                findUnique(j + 1, cur+[arr[j]], sum1+ arr[j])
                prevSum = arr[j]
    findUnique(0, [], 0)
    return result                     



if __name__ == "__main__":
    arr = [10,1,2,7,6,1,5]
    target = 8
    print(combinations(arr, target))