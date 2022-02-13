class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

def preOrder(temp):

    if temp:
        print(temp.data)
        preOrder(temp.left)
        preOrder(temp.right)

def inOrder(temp):
    if temp:
        inOrder(temp.left)  
        print(temp.data)
        inOrder(temp.right)    

def postOrder(temp):
    if temp:
        postOrder(temp.left)
        postOrder(temp.right)     
        print(temp.data)   


if __name__ == "__main__":
   root = Node(100)
   root.left = Node(90)
   root.right = Node(80)
   root.left.left = Node(70)
   root.right.left = Node(60)
   root.right.right = Node(50)
   print("\n Preorder Traversal of tree : ")
   preOrder(root)

   print("\n Ineorder Traversal of tree : ")
   inOrder(root)

   print("\n Postorder Traversal of tree : ")
   postOrder(root)
