class Node:

    def __init__(self, data ) -> None:
        self.data = data 
        self.left = None
        self.right = None

def inOrder(current):
    if current == None:
        return []
    inOrder(current.left) 
    print(current.data, end = " ")
    inOrder(current.right) 

def deletNode(root, node):
    q = []
    q.append(root)
    while len(q):
        current = q.pop()
        if current is node:
            current  = None
            return 

        if current.right:
            if current.right is node:
                current.right = None
                return 
            else:
                q.append(current.right) 

        if current.left:
            if current.left is node:
                current.left = None
                return  
            else:
                q.append(current.left)    


def deletion(root, key):
    if root == None:
        return 
    if root.left == None and root.right == None:
        if root.key == key :
            return None 
        else:
            return root 
    keyNode = None 
    q = []
    q.append(root)
    temp = None 
    while len(q):
        temp = q.pop()
        if temp.data == key:
            keyNode = temp 
        if temp.left:
            q.append(temp.left)     
        if temp.right:
            q.append(temp.right)

    if keyNode:
        x = temp.data 
        deletNode(root, temp) 
        keyNode.data = x
    return root 


if __name__ == "__main__":
    
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inOrder(root)
    key = 11
    root = deletion(root, key)
    print()
    print("The tree after the deletion;")
    inOrder(root)                                                              
                 

