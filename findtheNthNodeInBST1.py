class Node:

    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None 

count = [0]
def findNth(root, n):
    
    if root == None:
        return "Not found."

    if count[0] <= n[0]:
        findNth(root.left, n)  
        findNth(root.right, n)
        count[0] += 1
        if count == n:
            print(root.data)



if __name__ == "__main__":
    n = [2]
    root = Node(25)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(18)
    root.left.right = Node(22)
    root.right.left = Node(24)
    root.right.right = Node(32)
    print(findNth(root, n))
