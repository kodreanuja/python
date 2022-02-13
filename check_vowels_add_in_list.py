String = input()
def check_vowels(String):
    count = 0
    arr=[]
    vowels = set("AaEeIiOoUu")
    for i in String :
        if i in vowels:
            arr.append(i)
            count +=1
    print(count)        
    print(arr, end=" ")    
    
check_vowels(String)      


String1= (" This is my number 7709538822")
def check_number(String1):
    arr1=[]
    temp =0
    numbers = set("1234567890")
    for i in String1:
        if i in numbers :
            temp =temp+1
            arr1.append(i)
    print("\n", temp)        
    print(arr1, end = " ")
   
check_number(String1)    


        
      

