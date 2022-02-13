class Queue:


    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] *capacity 
        self.capacity = capacity 

    def isfull(self):
        return self.size == self.capacity
        
    def isEmpty(self):
        return self.size == 0

    def enQueue(self, item):
        if self.isfull():
            print("Queue is Full ")  
            return 

        self.rear = (self.rear + 1)  % (self.capacity)
        self.Q[self.rear] = item    
        self.size = self.size + 1
        print("% s enqued to queue " % str(item))     

    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty. ")
            return 
        print("%s deQueued " % str(self.Q[self.front])) 
        self.front = (self.front + 1)  % (self.capacity)      
        self.size = self.size -1


    def queueRear(self):
        if self.isEmpty():
            print("Queue is Empty.")   
        print("Rear is ", self.Q[self.rear])  

    def queueFront(self):
        if self.isEmpty():
            print("Queue is Empty ")
        print("Front is ", self.Q[self.front])           


if __name__ == "__main__":
    q = Queue(5)
    q.enQueue(10)
    q.enQueue(20)
    q.enQueue(30)
    q.enQueue(40)
    q.enQueue(50)
    q.deQueue()
    print("The above Queue is Full : ",q.isfull())
    print("the above queue is Empty : ",q.isEmpty())
    q.queueFront()
    q.queueRear()
    q.enQueue(70)
    print("The above is Full : ",q.isfull())