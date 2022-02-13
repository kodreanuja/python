def moveZero(array):
    return [nonZero for nonZero in array if nonZero!=0] + \
           [Zero for Zero in array if Zero==0]   
if __name__=="__main__":
    array= [] 
    size = int(input())  
    for i in range(size) :
        ele = int(input())
        array.append(ele)
    print("Original array : ",array) 
    print("Array with zero at the end of it: ",moveZero(array))   

def moveEven(array1):
    for ele in array1:
        if ele %2==0:
            right.append(ele)
        else:
            left.append(ele)    
    return left + right        

    
    
if __name__=="__main__":
    size = int(input())
    array1 = []
    left =  []
    right = []
    for i in range(size):
        ele = int(input())
        array1.append(ele)
        

    print("Original array : ", array1) 
    print("Array with Even  at the end of it: ",moveEven(array1))   


def movePrime(array2):
    for ele in array2:
        if ele == 2 and ele ==3:
            prime.append(ele)
        elif ele == 1  and ele == 0:
            nonprime.append(ele)    
        for i in range(2,int(ele/2)+1):
            if ele % i==0:
               nonprime.append(ele)
            else:
                prime.append(ele) 
            return nonprime + prime              
            
if __name__=="__main__":
    size = int(input())
    array2 = []
    nonprime = []
    prime = []
    for i in range(size):
        ele = int(input())
        array2.append(ele)
    print("Original array : ", array2) 
    print("Array with Even  at the end of it: ",movePrime(array2))   
    
    