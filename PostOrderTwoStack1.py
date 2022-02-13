class Node:
    
    def __init__(self, data) -> None:
        self.data = data 
        self.right = None 
        self.left = None 


def postOrder(root):
    if root == None:
        return 
    stack1 = []
    stack2 = []
    stack1.append(root)

    while len(stack1) != 0:
        i = stack1.pop()
        stack2.append(i)
        if i.left:
            stack1.append(i.left)
        if i.right:    
            stack1.append(i.right)
    while len(stack2) != 0:
        i = stack2.pop()
        print(i.data, end =" ")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    postOrder(root)      

