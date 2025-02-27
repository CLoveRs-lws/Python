n=int(input())
result=[]
used=set()
def backtrack(path,used):
    if len(path)==n:
        result.append(path.copy())
        return
    else:
        for i in range(1,n+1):
            if i not in used:
                used.add(i)
                path.append(i)
                backtrack(path,used)
                used.remove(i)
                path.pop()
backtrack([],used)
for stack in result:
    t=1
    s=[]
    i=0
    for j in range(1,n+1):
        s.append(j)
        while s and s[-1]==stack[i] and i<n:
            s.pop()
            i+=1
    if i==n:
        for x in range(n):
            if x!=n-1:
                print(stack[x],end=' ')
            else:
                print(stack[x])