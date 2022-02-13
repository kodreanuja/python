def union(arr1, arr2):
    if len(arr1) > 0 or len(arr2)> 0:
        for i in arr1:
            for j in arr2:
                if j not in arr1:
                    arr1.append(j)
    arr1.sort()
    return arr1           

if __name__ == "__main__":
    arr1 = [1, 3, 4, 5, 7]  
    arr2 = [2, 3,  5, 6] 
    #arr3 = []
    print(union(arr1, arr2)) 
    # union return all the element from both the array without repeatation.
