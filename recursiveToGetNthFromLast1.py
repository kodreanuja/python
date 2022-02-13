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

    def getNthFromLast(self, head, n):
        i = 0
        if (self.head == None):
            return 
        self.getNthFromLast(head.next, n) 
        i += 1   
        if i == n:
            return head.data 
       

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
    print(l.getNthFromLast(head.next,2))
    print(l.getNthFromLast(1))
    print(l.getNthFromLast(3))
    print(l.getNthFromLast(7))

