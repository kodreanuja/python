from queue import Queue
import sys

class pair(object):
    index = 0
    psf = " "
    jumps = 0

    def __init__(self, index, psf, jumps) -> None:
        self.index = index 
        self.psf = psf 
        self.jumps = jumps 

def minimumJum(arr):
        max_val = sys.maxsize
        dp = [0] *  len(arr)  
        n = len(dp)
        dp[n -1] = 0

        for i in range(n-2, -1, -1):
            steps = arr[i]
            min = max_val
            for j in range(1, steps+1, 1):
                if i + j >= n:
                    break 

                if dp[i+j] != max_val and dp[i+j] < min:
                    min = dp[i+j]

            if min != max_val:
                dp[i] = min + 1    

        return dp 

def possiblePath(arr, dp):
 
        queue = Queue(maxsize = 0)
        p1 = pair(0, "0", dp[0])
        queue.put(p1)
 
        while queue.qsize() > 0:
            tmp = queue.get()
 
            if tmp.jumps == 0:
                print(tmp.psf)
                continue
 
            for step in range(1, arr[tmp.index] + 1, 1):
                if ((tmp.index + step < len(arr)) and (tmp.jumps - 1 == dp[tmp.index + step])):
               
                    p2 = pair(tmp.index + step, tmp.psf +" -> " + str((tmp.index + step)), tmp.jumps - 1) 
                    queue.put(p2)
 

def Solution(arr):
    dp = minimumJum(arr)
     
    possiblePath(arr, dp)   


if __name__ == "__main__":
     
    arr = [ 3, 3, 0, 2, 1,2, 4, 2, 0, 0 ]
    print(Solution(arr))                   


        
