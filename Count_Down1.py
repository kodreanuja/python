def count_down(x):
    if x==0:
        print("Done !")
        return 0
    else:
        print(x)
        count_down(x-1)
        
    
if __name__=="__main__":
    #stack = []
    x = int(input())
    print(count_down(x))