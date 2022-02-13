import math as mt
def countPairs(bracks, num):
    openn=dict()
    close=dict()
 
    cnt = 0
    for i in range(num):
        s = bracks[i]
 
        l = len(s)
        op,cl = 0,0
        for j in range(l):
            if (s[j] == '('):
                op+=1
            else:
                if (op):
                    op-=1
                else: 
                    cl+=1
        if (op and cl==0):
            if op in openn.keys():
                openn[op]+=1
            else:
                openn[op]=1
        if (cl and op==0):
            if cl in openn.keys():
                close[cl]+=1
            else:
                close[cl]=1
        if (op==0 and cl==0):
            cnt+=1
    cnt = cnt //2
    for it in openn:
        cnt += min(openn[it], close[it])
    return cnt

if __name__=="__main__":
    bracks= [")())", ")", "((", "((", "(", ")", ")" ]
    num = len(bracks)
    print(countPairs(bracks, num))