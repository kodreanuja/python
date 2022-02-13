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

    def getNthFromLast(self, n):
        l = 0
        current = self.head 
        while current is not None:
            current = current.next 
            l += 1
        if  n > l:
            return " Location not found within the list."
        
        current = self.head        
        for i in range(0, l-n):
            current = current.next 
        return current.data            


    def printList(self):
        current = self.head 
        while(current):
            print(current.data, "->", end = " ")
            current = current.next 


if __name__ == "__main__":
    l = LinkedList()
    l.push(2)
    l.push(1)
    l.push(6)
    l.push(9)
    l.push(4)
    l.printList()
    print("\n")
    print(l.getNthFromLast(2))
    print(l.getNthFromLast(1))
    print(l.getNthFromLast(3))
    print(l.getNthFromLast(7))

