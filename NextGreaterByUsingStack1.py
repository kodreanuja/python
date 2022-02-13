from collections import deque

def nextGreaterElemnt(arr):
    result = [-1] * len(arr)
    if len(arr) == 0:
        return  
    s = deque()   
    for i in range(len(arr)):
        while s and arr[s[-1]] < arr[i]:
            result[s[-1]] = arr[i]
            s.pop()
        s.append(i) 
    return " ".join(str(i) for i in  result)      

if __name__ =="__main__":
    arr = [2, 7, 12, 5, 8 ,4, 10,  6, 15]
    print(nextGreaterElemnt(arr))
