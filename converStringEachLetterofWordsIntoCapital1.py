def convertString(s1):
    if len(s1) == 0:
        return 0
    result=' '.join(word[0].upper() + word[1:] for word in s1.split())
    return result         

if __name__ == "__main__":
    t = int(input())   
    for i in range(t):
        s1 = input() 
    print(convertString(s1))     
