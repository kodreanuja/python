class StackNode:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Stack:
    def __init__(self):
        self.head = None 

    def isEmpty(self):
        if self.head == None:
            return True 
        else:
            return False 

    def push(self, data):
        New_node = StackNode(data) 
        New_node.next = self.head 
        self.head = New_node  
        print ("% d pushed to stack" % (data))


    def pop(self):
        if (self.isEmpty()):
            return float("-inf")  
        current = self.head 
        self.head = self.head.next 
        removed = current.data 
        return removed

    def peek(self):
        if (self.isEmpty()):
            return float("-inf") 
        return self.head.data      

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
 
print ("% d popped from stack" % (stack.pop()))
print ("Top element is % d " % (stack.peek()) )                

# time Complexity of all operatons is O(1)