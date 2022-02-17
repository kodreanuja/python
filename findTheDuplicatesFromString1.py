
from collections import Counter
def findDuplicates(String):
    String1 = []
    String2 = []
    if len(String) == 0:
       return 0

    if len(String) > 1:
        for i in String:
            if i not in String1:
                String1.append(i)
            else:
                String2.append(i)  
            
    String2 = set(String2)        
    return "".join(String2)
    

if __name__ == "__main__":
    String = "Great responsibility";  
    print(findDuplicates(String))