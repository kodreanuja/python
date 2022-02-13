def addCorespondingElemntFromSets(sets):
    print(sets)
    result = 0
    for i in range(len(sets)):
        for j in range(len(sets[i])):
            result = sets[j]  
    return result  
if __name__ == "__main__":
    sets_count = int(input()) 
    sets = []  
    for set in range(sets_count):
        set = input().split()
        sets.append(set) 
    print(addCorespondingElemntFromSets(sets))       
