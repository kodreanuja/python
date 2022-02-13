class Node:

    def __init__(self, data) -> None:
        self.key = data 
        self.right = None 
        self.left = None 
        

def inorder(temp):
    if not temp:
        return 
    inorder(temp.left)  
    print(temp.key, end = " ")
    inorder(temp.right) 

def insert(temp, key):
    if temp == None:
        root = Node(key) 
        return 
    q = []
    q.append(temp)

    while len(q) != None:
        temp = q[0]
        q.pop(0)
        if temp.left == None:
            temp.left = Node(key)
            break 
        else:
            q.append(temp.left)
        if temp.right == None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)  
    print("Inorder traversal before insertion:", end = " ")
    inorder(root)  
    key = 14
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)        

             

