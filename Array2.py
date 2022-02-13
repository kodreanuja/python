def reverseList(Array, start, end):
    if start >= end:
        return
    Array[start], Array[end] = Array[end], Array[start]
    reverseList(Array, start+1, end-1)

    Array = [1, 2, 5, 7, 6, 8, 9]
    print(Array)
    reverseList(Array, 0, 6)
    print("Reverse List is :")
    print(Array)
    
    

def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)



