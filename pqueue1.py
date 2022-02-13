import heapq

li = [1, 4, 7, 9, 5, 3]
heapq.heapify(li)

print("Created Heap is : ", end = " ")
print(list(li))

heapq.heappush(li,8)
heapq.heappush(li,2)
print("Modified Heap : ", end = " ")
print(list(li))


heapq.heappop(li)
print("Modified Heap : ", end = " ")
print(list(li))

heapq.heappop(li)
print("Modified Heap : ", end = " ")
print(list(li))

 
