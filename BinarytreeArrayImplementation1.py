tree = [None] * 10
def root(k):
    if tree[0] != None:
        print("Tree already had root.")
    else:
        tree[0] = k

def setLeft(k, i):
    if tree[i] == None:
        print("child is not at", (i* 2)+1, "No parent is found.")
    else:
        tree[(i* 2)+1]= k  

def setright(k, i):
    if tree[i] == None:
        print("Child is not at", (i *2)+2, "No Parent is found.")
    else:
        tree[(i*2)+2] = k


def printTree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end = " ")
        else:
            print("_", end = " ")

    print()



root("A")
setLeft("B", 0)
setright("C", 0)
setLeft("D", 1)
setright("E", 1)
setLeft("F", 2) 
setright("G", 2)                        
print(printTree())
         


