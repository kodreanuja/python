class Node:

    def __init__(self, data) -> None:
        self.data = data 
        self.head = None 


class linkedList:

    def __init__(self) -> None:
        self.head = None 

    def push(self, data):
        New_node = Node(data)
        New_node.next = self.head 
        self.head = New_node 


    def getMiddle(self, head):
        slow = head 
        fast = head 

        while fast.next:
            slow = slow.next 
            if fast.next.next.next :
                fast = fast.next.next 
            else:
                fast = fast.next 
        return slow                     



    def printList(self):
        current = self.head 
        while(current):
            print(current.data, "->", end = " ")
            current = current.next 

if __name__ == "__main__":
    l = linkedList()
    l.push(2)
    l.push(4)
    l.push(1)
    l.push(3)
    print("\n")
    l.printList() 
    print("\n middle element is : ", end = " ") 
    print(l.getMiddle())  