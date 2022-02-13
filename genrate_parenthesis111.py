def genrate_parenthesis(n):
    stack = []
    res = []
    def backtraking(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
        if openN  < n:
            stack.append("(")
            backtraking(openN+1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")  
            backtraking(openN, closedN+1)  
            stack.pop()
    backtraking(0,0) 
    return res       
if __name__=="__main__":
    n = int(input())
    print(genrate_parenthesis(n))
