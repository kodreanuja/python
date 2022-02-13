def find_length(string):
    count = 0
    l = len(string)-1
    Flag = False
    while(l !=0):
        if string[l] ==" ":
            return count
        else:
           count +=1
        l-=1 
    return count           
if __name__=="__main__":
    string = input()
    print(find_length(string))    