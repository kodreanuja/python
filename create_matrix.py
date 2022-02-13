matrix = []
for  i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)      


#flatten matrix
flatten_matrix = []
matrix1 =[[1, 2, 3], [4, 5], [6, 7, 8, 9]]
for sublist in matrix1:
    for val in sublist:
        flatten_matrix.append(val)
print(flatten_matrix)        



flatten_fruits = []

fruits = [["Mango", "Apple", "Guva"], ["greps", "bananas", "watermelone", "dragonfruit"]]
for sublist in fruits:
    for fruit in sublist:
        if len(fruit)>5:
            flatten_fruits.append(fruit)
print(flatten_fruits)            


# generator and list comprehnsions   
list=[i for i in range(10) if i%2==0]   # list
print(list)
list=[i for i in range(10) if i%2!=0]
print(list)



ge = (i for i in range(20) if i%2==0)  # genrator
for i in ge :
    print(i, end=" ")
print("********************")

ge = (i for i in range(20) if i%2!=0 )
for i in ge:
    print(i, end=" ")

print("*****************")    

from sys import getsizeof

comp = [i for i in range(1000)]    
x = getsizeof(comp)
print("x :", x)

expre = (i for i in range(1000))
y = getsizeof(expre)
print("y :", y)

