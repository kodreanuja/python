class Node:

    def __init__(self, data) -> None:
        self.left = None 
        self.right = None
        self.value = data 

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.value, end = " ")
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.value, end = " ")    

def preOrder(root):
    if root:
        print(root.value, end = " ")  
        preOrder(root.left)
        preOrder(root.right)    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Preorder traversal of binary tree is")
preOrder(root)
 
print ("\nInorder traversal of binary tree is")
inOrder(root)
 
print("\nPostorder traversal of binary tree is")
postOrder(root)                   