lis = list(map(int, input().split()))
dataset = lis

def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset)//2
        leftarr = dataset[:mid]          # from start to mid
        rightarr = dataset[mid:]         # from mid  to  end
        
        mergeSort(leftarr)
        mergeSort(rightarr)

        i = 0                        # index of left
        j = 0                        # index of right 
        k = 0
        while i < len(leftarr) and j < len(rightarr) :

            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i+=1
            else:
                dataset[k] = rightarr[j]
                j+=1
            k +=1

        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i+=1
            k+=1     

        while j < len(rightarr):
           dataset[k] = rightarr[j]
           j+=1
           k+=1  
mergeSort(dataset)
print(dataset)