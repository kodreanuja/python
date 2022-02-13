class Node:

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data 

def preOrder2(root):
    if (root == None):
        return[]
 
    s = []
    current = root
    
    while (len(s) or current != None):
    
        while (current != None):
         
            print(current.data, end = " ")
 
            if (current.right != None):
                s.append(current.right)
 
            current = current.left
                 
        if (len(s) > 0):
            current = s[-1]
            s.pop()
             


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.left.left = Node(70)
root.left.right = Node(50)
root.right.left = Node(60)
root.left.left.right = Node(80)
preOrder2(root)