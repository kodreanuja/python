class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    # we start we two pointers at same starting point
    def detectAndRemoveLoop(self):
        slow_pointer = self.head
        fast_pointer = self.head 
        

        # when both pointer are not Null continue the loop
        while(slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next 

        #at this point we found the loop
 
            if slow_pointer == fast_pointer:   
                self.removeLoop(slow_pointer)
                return 1

        return 0

    # create seprate function for removing loop
    def removeLoop(self, loopNode):
        ptr1 = loopNode 
        ptr2 = loopNode
        count = 1

        while(ptr1.next != ptr2):
            ptr1 = ptr1.next 
            count  += 1

        ptr1 = self.head 
        ptr2 = self.head
 
        for i in range(count):
            ptr2 = ptr2.next 

        while(ptr2.next != ptr1):
            ptr1 = ptr1.next 
            ptr2 = ptr2.next 


        while(ptr2.next != ptr1):
            ptr1 = ptr2.next 

        ptr2.next = None 


    def push(self,data):
        new_node = Node(data)  
        new_node.next = self.head 
        self.head = new_node 

    def countlen(self):
        count = 0
        current = self.head 
        while (current.next):
            count += 1
        return count          


    def printList(self):
        current = self.head 
        while(current):
            print(current.data, "-->", end = " ")   
            current = current.next 


if __name__ == "__main__":
    l = LinkedList() 
    l.push(10)
    l.push(13)
    l.push(7)
    l.push(4)
    l.push(8) 
    l.printList() 
    print(l.countlen())               


