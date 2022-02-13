# time Complexity of this approch is O(n^2)
def LongestPalllindromicSubString(String):
    result = " "
    resultLen = 0
    for i in range(len(String)):
        left , right = i , i
        while( left >= 0 and right < len(String) and String[left] == String[right]):
            if (right - left + 1) > resultLen:
                result = String[left : right + 1]
                resultLen = right - left + i
            left -= 1
            right += 1    

        left , right = i, i + 1 
        while (left >= 0 and right < len(String) and String[left] == String[right]):
            if (right - left + 1) > resultLen:
                result = String[left : right + 1]    
                resultLen = right - left + 1
            left -= 1
            right += 1    

    return result         


if __name__== "__main__":
    String = input()  
    print(LongestPalllindromicSubString(String))  