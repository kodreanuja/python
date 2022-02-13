l1 = []
size = int(input())
for i in range(0,size):
    ele = input()
    l1.append(ele)

print (list(enumerate(l1)))


temp = []
size1 = int(input())
for i in range(0, size1):
    ele = input()
    temp.append(ele)
for index, ele in enumerate(temp):
    print(str((index,ele)) ) 
     
print("List : ",list((index, ele)))

print("Set : ",set((index,ele)))
    
