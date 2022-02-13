def isPresent(String, Substring):
    if Substring in String:
        return True
    else:
        return False    




if __name__=="__main__":
    String = input()
    Substring = input()
    print(isPresent(String, Substring))