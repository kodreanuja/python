class Node:
    def __init__(self, value) -> None:
        self.value = value 
        self.right = None 
        self.left = None 
    
    # insertion.

    def insert(self, value):
        if self.value:
            if value  < self.value:
                if self.left == None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)    
            elif value > self.value:
                if self.right == None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)    

        else:
            self.value = value     


    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()     


if __name__ == "__main__":
    root = Node(12)
    root.insert(10)
    root.insert(15)
    root.insert(5)
    root.printTree()
