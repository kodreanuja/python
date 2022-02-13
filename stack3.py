# using flag
def isBalanced(exp):
    flag = True
    count = 0
    for i in range(len(exp)):
        if (exp[i] == '('):
            count += 1
        else:
            count -= 1
  
        if (count < 0):
            flag = False
            break
    if (count != 0):
        flag = False
  
    return flag
  
if __name__ == '__main__':
    exp1 = input()
    exp2 = input()
  
    if (isBalanced(exp1)):
        print("Balanced")
    else:
        print("Not Balanced")
  
    if (isBalanced(exp2)):
        print("Balanced")
    else:
        print("Not Balanced")      

