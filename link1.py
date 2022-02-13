class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self) -> None:
        self.head = None 

    def insert(self, i) : 
        new_node = Node(i)
        new_node.next = self.head
        self.head = new_node

    def add(self, i):
        new_node = Node(i)
        new_node.next  = self.head 
        self.head = new_node 

    def insertAfter(self, prev_node, i):
        if prev_node is None:
            return "   " 
        new_node = Node(i) 
        new_node.next = prev_node.next
        prev_node.next = new_node  

    def delete(self, key):
        temp = self.head 
        if temp is not None:
            if temp.data == key:
                self.head = temp.next 
                del temp
                return
            else:
                prev = None
                while temp:
                    nextnode = temp.next
                    if temp.data == key:
                        break
                    prev = temp
                    temp = nextnode
                if temp is None:
                    return
                prev.next = temp.next
                

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end = "") 
            temp = temp.next            




if __name__ == "__main__":
    data = list(map(int, input().split()))
    l = LinkedList() 
    for i in range(len(data)):
        l.insert(data[i])
    # l.delete(data[i])
    l.delete(8)

    #l.add(data[i])
    #l.insertAfter(l.head.next,data[i])
        
    l.printlist()
