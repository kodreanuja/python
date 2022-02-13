class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Stack:
    def __init__(self):
        self.head = Node("head")  
        self.size = 0    

    def __str__(self):
        current = self.head
        res = ""   
        while (current.next):
            res +=  str(current.next.data) + " -> "
            current = current.next 
        return res[:-3]    

    def getSize(self):
        return self.size


    def isEmpty(self):
        return self.size == 0     

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking From Empty stack.")  
        return self.head.next.value   

    def push(self, data):
        New_node = Node(data)
        New_node.next = self.head.next 
        self.head.next = New_node
        self.size += 1    

    def pop(self):
        if self.isEmpty():
            raise Exception ("Removing From Empty stack. ")
        remove =  self.head.next 
        self.head.next   = self.head.next.next
        self.size -= 1
        return remove.data  

if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    print("Present Total Elements count in the Stack : ",stack.getSize())
    print("Empty : ",stack.isEmpty())
 
    for j in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")

    print("Present Total Elements count in the Stack : ",stack.getSize())