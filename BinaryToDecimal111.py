def binaryToDecimal(num):
    return "{0:b}".format(int(num))
if __name__== "__main__":
    num = int(input()) 
    print(binaryToDecimal(num))   
    # without BuiltIn function.