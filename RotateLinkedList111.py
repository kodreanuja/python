class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None 




    def rotateList(head, k):

        if k == 0 :
            return 
        current = head 
        while (current.next):
            current = current.next 
        current.next = head 
        current = head 

        for i in range(k -1):
            current = current.next 
        head = current.next 
        current.next = None 
        return head 

    def push(head, data):
        New_node = Node(data)
        New_node.next = head 
        head = New_node
        return head

    def print(current):
        while(current != None):
            print(current.data, "->", end = " ")
            current = current.next     

if __name__ == "__main__":
    headr = None 
    for i in range(1, 10, 1):
        head = push(headr, i)            



