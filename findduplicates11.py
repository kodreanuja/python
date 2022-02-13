n = int(input())
arr = list(map(int, input().split()))

def finDuplicates():
    dict = {}
    for ele in arr:
        try:
            dict[ele] +=1
        except:
            dict[ele] = 1
    for i in dict:
        if dict[i] >1:
            print(i, end =" ")           
    print("\n")
finDuplicates()    

