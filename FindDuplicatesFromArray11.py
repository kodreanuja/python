def findDuplicates(arr):
    l = len(arr)
    temp = []
    isPresent = False
    for i in range(1, l):
        for j in range(i+1, l):
            if arr[i] == arr[j]:
                if arr[i] in temp:
                    break
                else:
                    temp.append(arr[i])
                    isPresent = True
    if isPresent:
        return temp 
    else:
        return "No duplicates"   

            
            
if __name__ == "__name__":
    N = int(input())  
    arr = list(map(int, input().split())) 
    print(findDuplicates(arr)) 