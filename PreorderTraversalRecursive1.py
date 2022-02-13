class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None 

def preOrder(root):
    if root == None:
        return []
    result = []

    while root.left == None and root.right == None:
        return [root.data]

    result.append(root.data)  

    if root.left is not None:
        result += preOrder(root.left)

    if root.right is not None:
        result += preOrder(root.right) 

    return result                 


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
      



