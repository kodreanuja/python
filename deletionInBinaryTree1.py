class Node:

    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

def inOrder(current):
    if current is None:
        return 
    inOrder(current.left)
    print(current.data, end = " ")
    inOrder(current.right)     

def deleteDeepest(root, d):
    q = []
    q.append(root)
    while(len(q)):
        current = q.pop(0)
        if current is d:
            current = None
            return 
        if current.left:
            if current.left is d:
                current.left = None
                return 
        if current.right :
            if current.right is d:
                current.right = None 
                return 
        else:
            q.append(current.left)    

def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None 
        else:
            return root 
    key_node = None
    q = []
    q.append(root)
    current = None
    while len(q):
        current = q.pop(0)
        if current.data == key:
            key_node = current 
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

    if key_node:
        x = current.data 
        deleteDeepest(root, current)
        key_node.data = x
    return root     
    
                        










        
