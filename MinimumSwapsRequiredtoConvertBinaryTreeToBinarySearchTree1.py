def inOrder(a, n, i):
    global v 
    if i >= n:
        return 
    inOrder(a, n, 2* i + 1) 
    v.append(a[i])
    inOrder(a, n, 2* i +2)   

def minSwaps():
    global v 
    t = [[0, 0] for i in range(len(v))]
    ans = -2
    for i in range(len(v)):
        t[i][0], t[i][1] = v[i], i

    t, i = sorted(t), 0
    while i < len(t):
        if i == t[i][1] :
            i += 1
            continue   
        else:
            t[i][0], t[t[i][1]][0] = t[t[i][1]][0], t[i][0]
            t[i][1], t[t[i][1]][1] = t[t[i][1]][1], t[i][1]

        if (i == t[i][1]):
            i -= 1
        i += 1
        ans += 1
    return ans 

if __name__ == '__main__':
     
    v = []
    a = [ 5, 6, 7, 8, 9, 10, 11 ]
    n = len(a)
    inOrder(a, n, 0)
 
    print(minSwaps())    


