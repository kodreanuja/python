class Node:
    def __init__(self, key) -> None:
        self.left = None 
        self.right = None 
        self.data = key 
root = Node(1)   
root.left = Node(2)
root.right = Node(3) 
root.left.left = Node(4)
print(root)