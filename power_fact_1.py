# Itrative
def power(num, pow):
    if num !=0:
        p = num**pow
        return p
    else:
        return 0    

if __name__=="__main__":
    num = int(input())  
    pow = int(input()) 
    print(power(num, pow))

print("************************************************")

# recursive 
def fact(num1):
    if num1 > 1:
        f = num1 * fact(num1 -1)
        return f
    else:
        return 1  
if __name__=="__main__":
    num1 = int(input())   
    print(fact(num1))     
print("____________________________________________________________")

# recusive 
def power1(num, pwr):
    if pwr == 0:
        return 1
    else:
        return  num * power1(num, pwr-1)
if __name__=="__main__" :   
    num = int(input()) 
    pwr = int(input())
    print(power1(num, pwr))   

