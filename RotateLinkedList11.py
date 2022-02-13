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

    def printList(self):
        current = self.head 
        while(current):
            print(current.data, "->", end = " ")
            current = current.next 

    def rotateLinkedlist(self, k):
        if k == 0:
            return 

        current = self.head 
        count = 1
        while (count < k and current):
            current = current.next 
            count += 1

        if (current is None):
            return 
        kthNode = current 

        while(current.next):
            current = current.next 
        current.next = self.head 
        self.head = kthNode.next 
        kthNode.next = None 


if __name__ == "__main__":
    k = int(input())
    l = LinkedList()
    for i in range(60, 0, -10):
        l.push(i)     

    print("The list is :", end = " ")   
    l.printList()
    print("")
    print("Rotated List is : ", end = " ")   
    l.rotateLinkedlist(k)
    l.printList()


