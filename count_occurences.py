String = input()
a = input()
b = input()
def count_occurences(String,a,b):
    count = 0
    for i in range(len(String)):
        if String[i:i+len(b)==b]:
            count+=1
        if String[i:i+len(a)==a]:
           print(count, end=" ")
print(count_occurences(String,a,b))
  
