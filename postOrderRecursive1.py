class Node:

    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None 

def postOrder(root):
    if root is None:
            return
    result = []

    if  root.left is not None:
        result += postOrder(root.left)

    if root.right is not None:
        result += postOrder(root.right)

    while root.left == None and  root.right == None:
        return [root.data ]
    result.append(root.data)
        
    return result       



if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)  
    print("Postorder traversal before insertion:", end = " ")
    print(postOrder(root))
    print()
