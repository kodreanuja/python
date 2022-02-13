class Node:
    def __init__(self,data):
        self.left = None
        self.right = None 
        self.data = data 
def inOrder(root):
    current = root 
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left 
        elif(stack):
            current = stack.pop()
            print(current.data, end = " ")
            current = current.right 
        else:
            break 
    print()    
root = Node(6)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(2)
root.right = Node(89) 
root.right.right = Node(9)
root.right.left = Node(7)
inOrder(root)
print("hello")
