class Node:

    def __init__(self, data) -> None:
        self.data = data 
        self.left =  None 
        self.right = None 
        
def preOrder(root):
    if root is None:
        return []
 
    stack = []
    stack.append(root)
 
    while(len(stack) != 0):
         
        i = stack.pop()
        print (i.data, end=" ")
    
        if i.right is not None:
            stack.append(i.right)
        if i.left is not None:
            stack.append(i.left)       
    

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)  
    print("Preorder traversal before insertion:", end = " ")
    print(preOrder(root))
    print()
