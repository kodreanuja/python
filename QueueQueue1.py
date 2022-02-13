from queue import Queue
q = Queue(maxsize = 5 )
print(q.qsize())
q.put(5)
q.put(10)
q.put(15)
print("\n Empty : ",q.empty())
print("\n Full : ",q.full())
q.put(20)
q.put(25)
print("Size is :",q.qsize())
print("\n Full : ",q.full())

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print("\n Empty : ",q.empty())
print(q.qsize())


