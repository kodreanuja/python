dp = []
def F(n):
    if dp[n -1] is not None:       # initial it not null because we store value at 0th and 1st
        return dp[n-1]             # return it
    
    dp[n-1] =  F(n-F(n -1))+ F(n-F(n -2))
    return dp[n -1]
    

if __name__ == "__main__":
    n = int(input())
    dp = [None]*n            # size 
    dp[0] = dp[1] = 1        # store value at 0th and 1st position 
    F(n)
    print(dp)
    