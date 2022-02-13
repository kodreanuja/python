def mergeIntervals(Intervals):
    Intervals.sort(key = lambda i : i[0])
    opt = [Intervals[0]]
    for start, end in Intervals[1:]:
        lastEnd = opt[-1][1]
        if start <= lastEnd:
            opt[-1][1] = max(lastEnd, end)
        else:
            opt.append([start, end ]) 
    return opt           
if __name__ == "__main__":
    Intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(mergeIntervals(Intervals)) 
    # timeComplexity = O(nlogn)   
