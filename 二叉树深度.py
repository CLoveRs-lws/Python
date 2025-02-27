n=int(input())
leaf=set()
length=0
class Treenode:
    def __init__(self):
        self.f=None
node=[Treenode() for _ in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    if a!=-1:
        node[a-1].f=node[i]
    if b!=-1:
        node[b-1].f=node[i]
    if a==-1 and b==-1:
        leaf.add(i)
for j in leaf:
    num=0
    w=node[j]
    while w!=None:
        num+=1
        w=w.f
        if num>length:
            length=num
print(length)