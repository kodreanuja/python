def combination(arr, target):
    result = []

    def findSum(i, cur, sum1):
     
        if sum1 == target:
            result.append(cur)
            return 

        elif sum1 > target:
            return 
        else:
            for j in range(i, len(arr)):
                  
                findSum(j, cur + [arr[j]],sum1 + arr[j] )  
                          
    findSum(0, [], 0)
    # print(len(result))    
    return result                 



if __name__ == "__main__":
    arr = [2, 4, 6, 8]
    target = 8
    print(combination(arr, target))


