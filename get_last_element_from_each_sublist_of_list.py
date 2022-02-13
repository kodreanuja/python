def get_Last(list1):
    return [ele[-1] for ele in list1]
list1 = [[1, 2, 3], [7, 9, 5], [3, 6, 9]]
print(get_Last(list1)) 


def get_last1(list2):
    return [ele1[-1]for ele1 in list2]
list2= [[2, 4, 6], [1, 5, 9]]   
print (get_last1(list2))    


def get_first(list3):
    return[ele[0] for ele in list3]
list3 = [[1, 3, 5], [5, 7, 9], [9, 3, 6]]    
print(get_first(list3))




#using zip()
def Extract(lst):
    return list(zip(*[reversed(el) for el in lst]))[0]
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(Extract(lst))


def Islast(l):
  return list(zip(*[reversed(ele) for ele in l]))[0]
l = [[1, 5, 7, 9], [2, 4, 6, 8]]  
print(Islast(l))  


def Islast1(li):
   return (list(zip(*[reversed(ele) for ele in li])))[0]
   
li = [[2, 4, 6], [1, 2, 3]]    
Islast1(li)


# zip with map function.
def extract_last(lis):
    return (list(zip(*map(reversed,lis))))[0]
lis = [[1, 3, 5], [2, 5, 7]]
print(extract_last(lis))

