class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None 

class linkedList:

    def __init__(self) -> None:
        self.head = None 


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node 

    def printList(self):

        current = self.head 
        while(current):
            print(current.data, "-->", end = " ") 
            current = current.next    


    def detectLoop(self):
        s = set()
        current = self.head 

        while(current):

            if current in s:
                return True
            s.add(current)
            current = current.next 

        return False   


if __name__ == "__main__":
    l = linkedList() 
    l.push(10)
    l.push(3) 
    l.push(6)
    l.push(7)  
    l.printList()
    print("")

    # create loop for testing 
    l.head.next.next.next = l.head 
    
    if l.detectLoop():
        print("Loop is found. ")
    else:
        print("Loop is not found. ")              
