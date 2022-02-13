def maximumSumSubArray(arr):
    l = len(arr)                        # length of given array
    start = arr[0]                      # we start from starting index 
    max_end = 0                         # maximum end is 0
    for i in range(0, l):               # itrate over an array 
        max_end = max_end + arr[i]      # we start from 1st upto last add ele one bye one  
        if start < max_end:
            start = max_end
        elif max_end < 0 :
            max_end = 0
    return start        

if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]  
    print(maximumSumSubArray(arr))   