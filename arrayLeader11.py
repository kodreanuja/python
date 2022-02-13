from abc import ABCMeta


def leaders(arr,N):
    l = len(arr)
    temp = []
    for i in range(0, l):
        for j in range(i, l):
            if arr[i] < arr[j]:
                break
            if j == l-1:
                temp.append(arr[i])
    if len(temp) != 0:
        return " ".join(str(x) for x in temp) 
    else:
        return -1               



if __name__ == "__main__":
    N = int(input())  
    arr = list(map(int, input().split()))
    print(leaders(arr, N))   

        