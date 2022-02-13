def fibonacciTriangle(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return fibonacciTriangle(i - 2) + fibonacciTriangle(i - 1)



if __name__ == "__main__":
    i = int(input())
    print(fibonacciTriangle(i))    