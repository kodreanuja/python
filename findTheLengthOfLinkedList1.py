class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, New_data) :
        New_node = Node(New_data)
        New_node.next = self.head 
        self.head = New_node 

    def append(self, New_data):
        New_node = Node(New_data) 
        if (self.head == None):
            self.head = New_node
        last = self.head 
        while(last.next):
            last = last.next 
        last = New_node       

    def getsize(self):
        temp = self.head 
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count     


    def printList(self):
        temp = self.head 
        while(temp):
            print(temp.data, "->", end = " ")
            temp  = temp.next    

if __name__ == "__main__":
    l = LinkedList()
    l.append(100) 
    l.append(200) 
    l.add(10)
    l.add(20)
    l.add(30)
    l.add(40) 
    l.add(50) 
    l.printList()
    print(l.getsize())

