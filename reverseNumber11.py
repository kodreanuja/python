def reverseNumber(Num):
    rev = 0
    while  Num > 0:
        a = Num % 10
        rev = rev * 10 + a
        Num = Num // 10  
    if Num < 0:
        Num = str(Num) 
        rev = Num[::-1]
        return f"{Num[0]}{rev[:-1]}"

    return rev    

if __name__ == "__main__":
    Num = int(input()) 
    print(reverseNumber(Num))   