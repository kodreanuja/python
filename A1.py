import array as arr
a = arr.array('i', [2, 5, 7, 9])
print("the new Created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()    

b = arr.array('d', [12.2, 23.1, 45.0, 34.6, 56.2, 78.4])
print("The new created array is : ", end="")
for j in range(0, 6):
    print(b[j], end=" ")
print()