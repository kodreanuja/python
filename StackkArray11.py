from sys import maxsize

def createStack():
    stack = []
    return stack 

def isEmpty(stack):
    return len(stack) ==0    

def push(stack, item):
    stack.append(item)
    print(item)

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack.pop()  

def peek(stack):
    if isEmpty(stack):
          return str(-maxsize -1)    
    return stack[len(stack) -1] 


stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
push(stack, str(50))
print("Initial stack : ",stack)
print(pop(stack) + " is popped from stack")
print(pop(stack) + " is popped from stack")
print("Stack After removing element : ",stack)    

