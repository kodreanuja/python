class Queue:

    def __init__(self, size):
        self.queue = []
        self.front = 0
        self.rear = 0
        self.size = size

    def isFull(self):
        return self.size == self.rear

    def isEmpty(self):
        return self.front == self.rear    

    def enqueue(self, data):

        if self.isFull == True :
            return " Queue is Full "

        else:
            self.queue.append(data) 
            self.rear += 1

    def dequeue(self):
        if self.isEmpty == True:
            return "queue is Empty"
        else:
            self.queue.pop(0)
            self.rear -= 1   


    def display(self):

        if self.isEmpty == True:
            return "Queue is empty."

        for i in self.queue:
            print(i, "-->", end = " ")   


    def queueFront(self):
        if self.isEmpty == True:
            return "Queue is Empty " 
        else:
            return self.queue[self.front]   


    def queueRear(self):

        if self.isEmpty == True:
            return "Queue is Empty."   
        else:
            return self.queue[-1  ]             




            


if __name__ == "__main__":
    size = int(input())
    q = Queue(size)
    q.display()
    print("\n check queue is Empty : ",q.isEmpty())
    q.enqueue(40) 
    q.enqueue(56)
    q.enqueue(30)
    q.enqueue(12)
    print("Initial queue : ", end = " ")
    q.display()
    print("\n check queue is Full : ",q.isFull())
    print("\n Front element of the queue : ",q.queueFront())
    q.dequeue()
    q.dequeue()
    print("queue After deletion of some elements : ", end = " ")
    q.display()
    print("\n check queue is Empty : ",q.isEmpty())
    print("\n check queue is Full : ",q.isFull())
    print("Front element of the queue :",q.queueFront())
    print("Rear element of the queue :",q.queueRear())