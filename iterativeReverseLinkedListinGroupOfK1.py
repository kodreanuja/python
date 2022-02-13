class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None 
 
    def reverse(self, head, k):
        current = head 
        prev = None  
        tail = None 
        New_head = None 
        join = None 
        t = 0
        
        while(current):
            t = k
            join = current 
            prev = None 

            while(current and t > 0):
                temp = current.next 
                current.next = prev 
                prev = current 
                current = temp 
                t -= 1

            if (New_head == None):
                New_head = prev 

            if (tail != None):
                tail.next = prev 

            tail = join

        return New_head                
    
    def push(self, data):
        New_node = Node(data)
        New_node.next = self.head 
        self.head = New_node

    def printList(self):
        current = self.head 
        while(current):
            print(current.data, "-> ", end = "")
            current = current.next 


if __name__ == "__main__":

    l = LinkedList()
    l.push(1) 
    l.push(7)
    l.push(3)
    l.push(4)
    l.push(2) 
    l.push(5)  
    print("Original list : ")
    l.printList()
    print("\n Reversed list : ")
    l.head = l.reverse(l.head, 3)
    l.printList()
   

  






