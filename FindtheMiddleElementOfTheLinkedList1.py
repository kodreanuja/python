class Node:

    def __init__(self, data) -> None:
        self.data = data 
        self.next = None 

class LinkedList:

    def __init__(self) -> None:
        self.head = None    

    def push(self, data):

        New_node = Node(data)
        New_node.next = self.head 
        self.head = New_node 

    def getCount(self):
        count = 0
        current = self.head 
        while current:
            count += 1
            current = current.next 
        return count 


    def getMiddle(self):
        count = 0
        current = self.head 
        while current:
            count += 1
            current = current.next 
        middle = self.head    
        while count//2:
            middle = middle.next
            return middle.data  

    "How to get the middle element, I got index "       


    def printlist(self):
        current = self.head 
        while(current):
            print(current.data, "->", end = " ")
            current = current.next


if __name__ == "__main__":
    l = LinkedList()
    l.push(3)
    l.push(5)
    l.push(4) 
    l.printlist() 
    print("\n size of the given linked list is : ", end = " ") 
    print(l.getCount()) 
    print("\n middle element is : ", end = " ") 
    print(l.getMiddle())     

