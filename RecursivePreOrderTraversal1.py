class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None 

def preOrder(root):

    if root is not None:
        print(root.data , end = " ")
        preOrder(root.left)
        preOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
preOrder(root)