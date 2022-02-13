class Node:

    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 

def postOrderItretive(root):
    stack = []

    while(True):

        while(root != None):
            stack.append(root)
            stack.append(root)
            root = root.left
 
       
        if (len(stack) == 0):
            return
         
        root = stack.pop()
 
        if (len(stack) > 0 and stack[-1] == root):
            root = root.right
        else:
            print(root.data, end = " ")
            root = None
   
    


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7) 
    print("Postorder traversal :", end = " ")
    print(postOrderItretive(root))
    print()