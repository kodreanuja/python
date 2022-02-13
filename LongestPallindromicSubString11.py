#Brute force algorithm 
# time complexity = O(n^3)
# we can optimize this time complexity 

def printSubStr(String, low, high):
     
    for i in range(low, high + 1):
        print(String[i], end = "")

def longesPallindrome(String):
    l = len(String)
    maxLength = 1
    start = 0
    for i in range(l):
        for j in range(i, l):
            flag = 1

            for k in range(0, ((j - i) // 2) + 1):
                if String[i + k] != String[j - k]:
                    flag = 0

            if flag != 0 and (j - i + 1) > maxLength:
                start = i
                maxLength = j - i + 1        
        
    printSubStr(String, start, start + maxLength - 1)

    print("\n")

    return maxLength    

if __name__ == "__main__":
    String = input()
    print(longesPallindrome(String))