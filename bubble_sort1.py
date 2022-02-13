def bubbleSort(lis):
    for i in range(len(lis)-1, 0, -1):
        for j in range(i):
            if lis[j] > lis[j+1]:
                temp = lis[j]
                lis[j]= lis[j+1]
                lis[j+1]= temp
            print("Current_state : ", lis)
if __name__=="__main__":
    lis = list(map(int, input().split()))
    print(bubbleSort(lis))

# for loop inside for loop it takes O(n^2) time to run.
# there for runtime for bubble sort is O(n^2).
def bubbleSort1(dataset):
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1]= temp
    return dataset            
if __name__=="__main__":
    lis = list(map(int, input().split()))  
    dataset = lis
    print(bubbleSort1(dataset))     