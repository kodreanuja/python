def power(a, b):
    if a == 0 and b == 0:
        return 0 
    return pow(b, a)    


if __name__ == "__main__":
    a = 10
    b = 2.000
    print(power(a, b))