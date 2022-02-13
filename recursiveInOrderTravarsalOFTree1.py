class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
def inOrder(root):
    if  root is not None :
        inOrder(root.left)
        print(root.data, end = " ")
        inOrder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  
inOrder(root)              