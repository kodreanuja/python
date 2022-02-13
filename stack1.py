stack = []
stack.append(20)
stack.append(15)
stack.append(10)
stack.append(5)
print(stack)
x = stack.pop()
print(x)
print(stack)
x = stack.pop()
print(x)
print(stack)
def stackempty(stack):
    while(stack != []):
        x= stack.pop()
        print(x)
    return "".join(stack)
if __name__=="__main__":
    stack = list(map(int, input().split())) 
    print(stackempty(stack))
