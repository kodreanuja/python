def DevideTwoInt(dividend,divisor):
    if divisor < 0:
        
            if dividend < 0:
                 result = dividend // divisor
            else:
                 result = (dividend // (divisor * -1)) * -1
    
    else:
       
            if dividend < 0:
                 result = ((dividend*-1) // divisor) * -1
            else:
            
                 result = dividend // divisor
   
    if result >= 2147483648:
        result -= 1
    return result

if __name__ == "__main__":
     dividend = int(input())
     divisor = int(input())    
     print(DevideTwoInt(dividend, divisor))