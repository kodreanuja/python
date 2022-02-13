class Node:

    def __init__(self, data, left= None, right= None):
        self.data = data 
        self.left = left 
        self.right = right 

def MorriesTraversal(root):

    current = root

    while current != None:

        if current.left == None:
            print(current.data)
            current = current.right 
        else:
            i = current.left 
            while i.right is not None and i.right != current:
                i = i.right 

                if i.right == None:
                    i.right = current 
                    current = current.left
                else:
                    i.right = None
                    print(current.data)
                    current = current.right     


root = Node(1,right=Node(3),left=Node(2,left=Node(4),right=Node(5)))
  
for v in MorriesTraversal(root):
    print(v, end=' ')

