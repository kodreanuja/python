class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
         self.head = None

    def traverse(self):
        
        linkedListStr = ""
        temp = self.head
        
        while temp:
            linkedListStr += str(temp.data) + " -> "
            temp = temp.next
            
        return linkedListStr + "NULL"

    def insert(self, data):
        
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

def reverse(Head):
    
    if (Head is None and 
        Head.next is None):
        return Head
        
    prev = None
    curr = Head
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    Head = prev
    return Head

def listSum(l1, l2):

    if l1 is None:
        return l1
    if l2 is None:
        return l2


    l1 = reverse(l1)

    l2 = reverse(l2)

   
    head = l1
    prev = None
    c = 0
    sum = 0
    
    while l1 is not None and l2 is not None:
        sum = c + l1.data + l2.data
        l1.data = sum % 10
        c = int(sum / 10)
        prev = l1
        l1 = l1.next
        l2 = l2.next
        
    if l1 is not None or l2 is not None:
        if l2 is not None:
            prev.next = l2
        l1 = prev.next
        
        while l1 is not None:
            sum = c + l1.data
            l1.data = sum % 10
            c = int(sum / 10)
            prev = l1
            l1 = l1.next
            
    if c > 0:
        prev.next = Node(c)
        
    return reverse(head)

    
linkedList1 = LinkedList()
linkedList1.insert(3)
linkedList1.insert(6)
linkedList1.insert(5)
print("LinkedList1 : ", end = " ")

linkedList2 = LinkedList()
linkedList2.insert(2)
linkedList2.insert(4)
linkedList2.insert(8)

linkedList3 = LinkedList()
linkedList3.head = listSum(linkedList1.head,linkedList2.head)
                           
print(linkedList3.traverse())
 
   
 
    
       
 
