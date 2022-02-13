class Node:

    def __init__(self, val) -> None:
        self.left = None 
        self.right = None 
        self.val = val 

def inorder(root):
    if root is None:
        return []
    result = []

    if root.left is not None:
        result += inorder(root.left)  

    result += [root.val]     

    if root.right is not None:
        result +=inorder(root.right)

    return result 


def insert(temp,val):
    if temp == None:
        root = Node(val)
        return 
    q = []
    q.append(temp)
    while len(q) != None:
        temp = q[0]
        q.pop(0)
        if temp.left == None:
            temp.left = Node(val)
            break 
        else:
            q.append(temp.left)

        if temp.right == None:
            temp.right = Node(val)
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
    print(inorder(root)) 
    key = 14
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    print(inorder(root))        

             



              