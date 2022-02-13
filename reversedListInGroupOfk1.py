class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self) -> None:
        self.head = None 

    def reverse(self, head, k):
        if head == None:
            return None 
        current = head 
        prev = None 
        next = None 
        count = 0

        while(current != None and count < k):
            next = current.next 
            current.next = prev 
            prev = current 
            current = next 
            count += 1

        if next is not None:
            head.next = self.reverse(next, k)    
        return prev 

    def push(self, data):
        New_node = Node(data)
        New_node.next = self.head 
        self.head = New_node 

    def printlist(self):
        current = self.head 
        while(current):
            print(current.data, "->", end = " ")
            current = current.next 


if __name__ == "__main__":
    l = LinkedList()
    l.push(10)
    l.push(5)
    l.push(9)
    l.push(4)
    l.push(6)
    l.push(7)
    print("Original list : ")
    l.printlist()
    print("\n Reversed list : ")
    l.head = l.reverse(l.head, 3)
    l.printlist( 2)



