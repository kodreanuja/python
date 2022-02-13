class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:
    def __init__(self):
        self.head = None
    
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
     
    def push(self,data):
         
        if self.head == None:
            self.head=Node(data)
             
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
         
        if self.isempty():
            return None
             
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
     
    def peek(self):
         
        if self.isempty():
            return None
             
        else:
            return self.head.data
       
    def display(self):
         
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
         
        else:
             
            while(iternode != None):
                 
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return   

if __name__ == "__main__":
    s =   Stack()
    s.push(10)
    s.push(20) 
    s.push(40)
    s.push(50)
    s.display()
    print("\n Poped elements : ")
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("stack After poping elements :")
    s.display()
    print("\n")
    print("top of the stack is :" ,end = "")
    print(s.peek())



