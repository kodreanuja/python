def  addBinary(a, b):
    sum = bin((int(a, 2)) +(int(b, 2)))
    return sum[2:]
if __name__ == "__main__":
    a = "11"
    b =  "1"
    print(addBinary(a, b))


       