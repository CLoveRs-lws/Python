n=int(input())
leaf=set()
length=0
rela={}
for i in range(n):
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        leaf.add(i)
    else:
        for j in {a,b}:
            if j!=-1:
                rela[j]=i
num=len(leaf)
for i in leaf:
    l=0
    while i in rela:
        l+=1
        i=rela[i]
        if l>length:
            length=l
print(length,num,sep=' ')
