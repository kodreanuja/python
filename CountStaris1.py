def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2) 
def countStairs(n):
    return fib(n + 1) 

if __name__ == "__main__":
    n = int(input())   
    print(countStairs(n))       
    