def fibonacciNumber(Num):
    if (Num == 0):
        return 0
    elif (Num == 1):
        return 1
    else:
        return fibonacciNumber(Num - 1) + fibonacciNumber(Num - 2)         
if __name__ == "__main__":
    Num = int(input())  
    print(fibonacciNumber(Num))  