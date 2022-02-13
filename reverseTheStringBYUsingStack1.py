def createStack():
    stack = []
    return stack 

def sizeOFStack(stack):
    return len(stack)  


def isEmpty(stack):
    if len(stack) == 0:
        return True 
    else:
        return False 


def push(stack, i):
    stack.append(i) 

def pop(stack):
    if isEmpty == True:
        return 
    else:
        return stack.pop()

def reverse(String):
    n = len(String) 
    stack = createStack()

    for i in range(0, n, 1):
        push(stack, String[i])

    rev  = " "

    for i in range(0, n, 1):
        rev += pop(stack)

    return rev   


if __name__ == "__main__":
    String = "algorithms and structures data"
    String = reverse(String)
    print("Reverse String is :", String )
    


