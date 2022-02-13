from collections import deque

stack = deque()
stack.append(1)
stack.append(3)
stack.append(5)
stack.append(7)
stack.append(9)
print("Initial stack : ", stack)
print("Removing the element from the stack : ")
print(stack.pop())
print(stack.pop())
print(stack.popleft())
print("Stack : ", stack )