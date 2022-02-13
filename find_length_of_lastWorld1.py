def findLength(string):
    l = 0
    s= string.strip()
    for i in range(len(s)):
        if s[i]==" ":
            l=0
        else:
            l+=1
    return l 
if __name__=="__main__":
    string = input()
    print(findLength(string))               
