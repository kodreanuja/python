def even(num, lis):
    while True:
        if num %2==0:
            lis.appendleft(num)
        else:
            lis.append(num)
            return "".join(lis)

if __name__=="__main__":
    lis = list(map(int, input().split())) 
    num = int(input()) 
    print(even(num, lis))  