list1 = []
size1 = int(input(" Enter your 1st list size : "))
for  i in range(0, size1):
   ele = input("pass list1 ")
   list1.append(ele)
print(list1)

list2 = []
size2 = int(input("Enter your 2nd list size : "))
for j in range(0, size2):
    ele1 = input(" pass list2 ")
    list2.append(ele1)
print(list2)  

ele_indices = dict()
for index, val in enumerate(list1):
   ele_indices.setdefault(val,[]).append(index)
res = [ele_indices.get(index, [None]) for index in list2]   

print(res)    
