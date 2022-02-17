def addbinary(B1, B2):
    maxL = max(len(B1), len(B2))
    a = B1.zfill(maxL)
    b = B2.zfill(maxL)
    result = ""
    carry = 0
    for i in range(maxL - 1, -1, -1):
        r = carry 
        r += 1 if a[i] == "1" else 0 
        r += i if b[i] == "1" else 0 
        result = ("1" if r%2 == 1 else "0") + result 
        carry = 0 if r < 2 else 1 
    if carry != 0 :
        result = "1" + result 
    return (result.zfill(maxL))   


"""By Using Built in Functions: """

def binary(B1, B2):
    sum = bin(int(B1, 2)+ int(B2, 2))
    print(sum[2:])
    return sum

if __name__ == "__main__":
    B1 = "1101"
    B2 = "100"
    print(addbinary(B1, B2))
    print(binary(B1, B2))