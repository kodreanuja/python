def reverse(String):
    start = 0
    end = len(String) -1
    temp = []
    if len(String) == 0:
        print("String is Empty")
    else:    
        for i in String:
            temp.append(i)
        while start < end :
            temp[start] , temp[end] = temp[end] , temp[start]
            start += 1
            end -= 1
    return "".join(str(l) for l in temp)   
if __name__ =="__main__":
    String = input() 
    print(reverse(String))   

