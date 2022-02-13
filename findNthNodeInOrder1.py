class Node:

    def __init__(self, data) -> None:
        self.data = data 
        self.left = None 
        self.right = None 
count = [0]
def findNthInOder(root, n):

    if root == None:
        return 

    if count[0] <= n:

        findNthInOder(root.left, n)

        count[0] += 1  

        if count[0] == n:
            print(n, "node of this tree is  : ",root.data)

        findNthInOder(root.right, n)  


if __name__ == "__main__":
    n = int(input())
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
 
    print(findNthInOder(root, n))