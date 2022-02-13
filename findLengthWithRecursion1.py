class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, New_data):
        New_node = Node(New_data) 
        if (self.head  is None):
            self.head  = New_node
            return
        last = self.head     
        while(last.next):
            last  = last.next 
        last.next  = New_node 

    def getsize(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getsize(node.next)  

    def getCount(self):
       return self.getsize(self.head)            

    def printList(self):
        temp = self.head 
        while(temp):
            print(temp.data, "->", end = " ")  
            temp = temp.next    

if __name__ == "__main__":
    l = LinkedList()
    data = list(map(int, input().split()))
    for New_data in range(len(data)):
        l.append(data[New_data])
    l.printList()
    print("\n The length of the linkedList is : ", end = "")
    print(l.getCount())






