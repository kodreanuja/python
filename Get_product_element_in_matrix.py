def prod(val) :
    result = 1 
    for ele in val:
        result *= ele
    return result
test_list = [[3, 7, 6], [1, 3, 5], [9, 3, 2]]
  

print("The original list : " + str(test_list))
result = [prod(idx) for idx in zip(*test_list)]  
print(result)


# When you zip something, you bring both sides together.
# And that's how the zip() function works! It brings elements
# of the same index from multiple iterable objects together
# as elements of the same tuples. The zip() function
# takes in iterables as arguments, 
#such as lists, files, tuples, sets# 

def find_sum(value):
    result1 =0
    for ele in value:
        result1 +=ele
    return result1
list= [[3, 7, 6], [1, 3, 5], [9, 3, 2]]  
result1 =[find_sum(index) for index in zip(*list)] 
print(result1)      

def find_mod(value1):
    r = 0
    for ele in value1:
        r %= ele
    return r
list1 =   [[3, 7, 6], [1, 3, 5], [9, 3, 2]]  
r = [find_mod(index) for index in zip(*list1)]     
print(r)