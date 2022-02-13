# using tuple and map

def check(expression):
    open_tuple  = ("(","{", "[")
    close_tuple =  (")", "}", "]")
    map = dict(zip(open_tuple, close_tuple))
    queue = []
    
    for i in expression:
        if i in open_tuple:
            queue.append(map[i])
        elif i in close_tuple:
            if not queue or i != queue.pop():
                return "Unblanced"  

    if not queue:
        return "Balanced" 
    else:
        return "Unbalnced"              



if __name__=="__main__":
    expression = input() 
    print(check(expression))   