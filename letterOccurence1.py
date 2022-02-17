def charOccurence(String):
    d = {}
    for i in String:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for i in String:
 
        if d[i] != 0:
            print("{}{}".format(i,d[i]), end ="")
            d[i] = 0


if __name__ == "__main__":
    String = input()
    print(charOccurence(String))
