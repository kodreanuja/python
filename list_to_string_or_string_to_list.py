def convert(String):
    list1 = list(String.split(" "))
    return list1


if __name__=="__main__":
    String = (input())
    print(convert(String))
    
list2 = ["Anuja", "pritee"]    
print(str(list2))    


def list_to_String(list):
    str1 =" "
    for item in list:
        str1+=item
    return str1  
       

if __name__=="__main__":
    list=["Anuja", "pritee", "Muktai"]
    print(list_to_String(list))



def list_to_String1(list1):
    str1 =" "
    return str1.join(list1)
if __name__=="__main__":
    list1 = ["Anuja", "Pritee", "Muktai"]
    print(list_to_String1(list1))    




