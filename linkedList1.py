# class node 
class Node:
    def __init__(self,data):                                # function which initialize the node object
        self.data = data                                    # assigning the data
        self.next = None                                    # assigning next to  null

# class LinkedList
class LinkedList:
    def __init__(self) -> None:                            # This function initialize the linked list object
        self.head = None                                   # assigning head to None

#time complexity of add is O(1).          
    def add(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

# time complexity of insertAfter is O(1).    

    def insertAfter(self, prevNode, new_data):
        if prevNode is None:
            print("Previous node must be linked List")
            return 
        new_node = Node(new_data)  
        new_node.next = prevNode.next
        prevNode.next = new_node      

#  time complexity is O(n) because it travers through all the list.
    def  append(self, new_data):
        new_node = Node(new_data)    
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while(last.next) :
            last = last.next
        last.next = new_node    

# printList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end = "")
            temp = temp.next

if __name__ == "__main__":
    li = LinkedList()   
    li.append(12)
    li.append(14) 
    li.append(16) 
    li.insertAfter(li.head.next, 8)    
    li.printList()



