def addBinary(a, b):
    maxLen = max(len(a), len(b))
    a = a.zfill(maxLen)
    b = b.zfill(maxLen)
    result = " "
    carry = 0
    for i in range(maxLen-1, -1, -1):
        r = carry 
        r += 1 if a[i] == "1" else 0
        r += 1 if b[i] == "1" else  0
        result = ("1" if r%2 == 1 else "0") + result 
        carry = 0 if r < 2 else 1
    if carry != 0:
        result = "1" + result    
    return result.zfill(maxLen)     

if __name__ == "__main__":
    a = "11"
    b = "1"
    print(addBinary(a,b))
    # Output = 10001