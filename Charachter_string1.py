def newString(charSet, input1 ):
    original_charSet = "abcdefghijklmnopqrstuvwxyz"
    mapchar = dict(zip(original_charSet, charSet))
    changeChar = [mapchar[ch] for ch in input1]
    print("".join(changeChar))

if __name__=="__main__":
    charSet = 'qwertyuiopasdfghjklzxcvbnm' 
    input1 = input()
    newString(charSet,input1)
