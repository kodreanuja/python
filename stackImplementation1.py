class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
class Stack:
    def __init__(self):
        self.root = None 

    def isEmpty(self):
        if self.root == None:
            return True 
        else:
            return False 

    def push(self, data):
        New_node  = Node(data)
        New_node.next = self.root 
        self.root = New_node 
        print(data)

    def pop(self):
        if self.isEmpty == True:
            print("Can't pop element from empty stack.")
        current = self.root 
        self.root = self.root.next 
        i = current.data 
        return i 

    def peek(self):
        if self.isEmpty == True:
            return None 
        return self.root.data 
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print ("Top element is % d " % (stack.peek())) 
print ("% d popped from stack" % (stack.pop()))
stack.push(40)
print ("Top element is % d " % (stack.peek()))    
stack.push(50)
print ("Top element is % d " % (stack.peek()))  
print ("% d popped from stack" % (stack.pop())) 
print ("% d popped from stack" % (stack.pop()))             


                