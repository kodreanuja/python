from collections import deque  # it provides the feature to remove elemet from both the ends.
queue = deque()
queue.append(10)
queue.append(30)
queue.append(40)
queue.append(50)
print(queue)
queue.appendleft(60)          # it add the element at the left end.
print(queue)
queue.popleft()               # delet the elemet from left end.
print(queue)
print(queue.copy())           # makes the copy of queue
queue.reverse()               # reverse the list or any collection.
print(queue)
queue.append(10)
print(queue.count(10))        #  It gives the count of perticular elemet .
print(queue.clear())          # delete the whole queue.

def queue_empty(queue):
    while(queue !=[]):
        x = queue.pop()
        print(x)
    return "".join(queue)
if __name__=="__main__":
    queue= list(map(int, input().split()))
    print(queue_empty(queue))  
    #print(queue)   