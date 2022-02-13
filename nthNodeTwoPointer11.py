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
        main_ptr = self.head
        ref_ptr = self.head 
    
        count = 0 
        if(self.head is not None):
            while(count < n ):
                if(ref_ptr is None):
                    return  "% d is greater than the  no. pf nodes in list" %(n)
 
                ref_ptr = ref_ptr.next
                count += 1
    
        if(ref_ptr is None):
            self.head = self.head.next
            if(self.head is not None):
                return "Node no. % d from last is % d " %(n, main_ptr.data)
        else:
          

          while(ref_ptr is not None):
              main_ptr = main_ptr.next 
              ref_ptr = ref_ptr.next

          return "Node no. % d from last is % d "  %(n, main_ptr.data)
     

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

