list = []
size = int(input())
for i in range(0,size):
    ele = int(input())
    list.append(ele)
print(list) 
temp=[]   
arr =[]

# enumrate function which return the index starts by default 0 
# enumrate(itrable , start=0)

for index, ele in enumerate(list):
    if ele%2==0:
        temp.append(index)
        arr.append(ele)
print("Even element indices : ",str(temp)) 
print("even element list : ",str(arr))       
