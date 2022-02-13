items1 = dict({"key1":1, "key2":2, "key3": 3, "key4":4, "key5": "Five"})
print(items1)
items2 = {}
items2["key1"] = "one"
items2["key2"] = "Two"
items2["key3"] = "Three"
print(items2)
for key in items2.keys():              
    print(key)                   # print only keys
for value in items2.values():
    print(value)                 # print only value

details = {}
details["Name"] = "Anuja"
details["School"] = "Shri Keshvraj Vidhylay"
details["City"] = "Latur"
details["DBO"] = "23/05/1998"
print(details)
print(details["City"])
print(details["DBO"])
details["City"] = "Pune"
print(details)

for key, value in details.items():      
    print("key :", key ," ", "Value : " , value )       #print  both values and keys.

for key in details.keys():
    print(key, end = " ")
print(" ")    
for value in details.values():
    print(value, end = " ")    

