def decimalToBinary(num):
    return bin(num).replace("0b", "")
if __name__ == "__main__":
    num = int(input())
    print(decimalToBinary(num))  
    # By using Built in function.  