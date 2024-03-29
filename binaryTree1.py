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
    if not temp:
        root = Node(key)
        return 
    q = []
    q.append(temp)   

    while(len(q)):
        temp = q[0]  
        q.pop(0)  

        if(not temp.left):
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = Node(key) 
            break
        else:
            q.append(temp.right)  


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(6)
    root.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(4)
    print("Inorder traversal before insertion:", end = " ")
    inorder(root)
 
    key = 12
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)

