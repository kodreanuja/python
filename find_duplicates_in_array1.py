def findDuplicates(arr, size):
    l = len(arr)
    temp = []
    if l ==0:
        return -1
    else:
        for i in range(0, l):
            for j in range(i+1, l):
                if arr[i] == arr[j]:
                    temp.append(arr[i])
    temp.sort()  
    temp = set(temp)              
    t = len(temp)
    if t != 0:
        return " ".join(str(i) for i in temp)
    else:
        return -1               

if __name__ == "__main__":
    size = int(input())
    arr = list(map(int, input().split()))
    print(findDuplicates(arr, size))    