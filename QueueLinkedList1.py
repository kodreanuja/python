class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None   

    def isEmpty(self):
        return self.front == None

    def enQueue(self, data):
        Current  = Node(data) 
        if self.rear == None:
            self.front = self.rear = Current 
            return 
        self.rear.next = Current 
        self.rear = Current

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Removing from empty Queue is Not possible.")  
        Current = self.front 
        self.front = Current.next
        
        if (self.front == None):
            self.rear = None 

    def printQueue(self):
        current = self.front 
        while(current):
            print(current.data, "->", end = " ")
            current = current.next 

if __name__ == "__main__":
    q = Queue()
    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)
    print("Initial Queue: ", end = "")
    q.printQueue()
    print("\n")
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))
    q.deQueue()
    q.deQueue()
    q.printQueue()
                      

