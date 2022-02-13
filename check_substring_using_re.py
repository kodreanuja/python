import re

String = input()
Substring = input()
if re.search( Substring,String):
    print("Yes".format(Substring, String))
else:
    print("No".format(Substring,String))    



