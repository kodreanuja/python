
# itmgetter = use to get the perticular item from the list .
from operator import itemgetter
def getlast(lis):
    return(list(map(itemgetter(-1), lis)))
lis  = [[1, 3, 7], [2, 4, 8]] 
print(getlast(lis))   

def getfirst(lis):
    return list(map(itemgetter(0), lis))
lis = [[2, 3, 5], [2, 4, 6],  [1, 3, 5]]  
print(getfirst(lis))

def get_middle(lis):
    return list(map(itemgetter(0)), lis)
lis = [[2, 4, 6]]    
print(get_middle(lis))