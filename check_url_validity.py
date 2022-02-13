import re
def url_validity(String):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
    patern = re.compile(regex)
    if String==None:
        return False
    if re.search(patern,String) :
        return True
    else:
        return False      

if __name__=="__main__":
    String =input()
    if (url_validity(String)==True):
        print("Yes")
    else:
        print("No")  

  #'''The purpose of the compile method is to compile the regex pattern which will be
  # used for matching later. It's advisable to compile regex when it'll be used several times in your program. 
  #Resaving the resulting regular expression object for reuse, which re. compile does, is more efficient.10-Feb-2017'''       

