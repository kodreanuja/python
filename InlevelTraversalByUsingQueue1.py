class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

def levelOrderTraversal(root):
    if root is None:
        return 
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)   

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(9)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)

    print("LevelOrder Traversal")
    levelOrderTraversal(root )
