def gcd(a, b):
    while b !=0:
        temp = a
        a = b
        b = temp % b
    return a
if __name__=="__main__":
    a = int(input())
    b = int(input())
    print(gcd(a, b))
