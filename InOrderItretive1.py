class Node:

    def __init__(self, data ) -> None:
        self.data = data 
        self.left = None 
        self.right = None

def inOrder(root):
    stack = []
    current = root 
    while (True):
        if current != None:
            stack.append(current)
            current = current.left 

        elif current == None and len(stack)!= 0:
            current  = stack.pop()
            print(current.data, end = " ")
            current = current.right
        else:
            break



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    inOrder(root)          




