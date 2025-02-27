x=list(map(int,input().split()))
a,b,c,d=x[1],x[0],x[3],x[2]
i=2
List=1
list=[]
m,n=a,c
p=b*c+a*d
q=a*c
while(i<=n and i<=m):
    if n%i==0 and m%i==0:
        n=n//i
        m=m//i
        list.append(i)
        List*=i
    else:
        i+=1
if list==[]:
    print(p,q,sep='/')
else:
    p=p//List
    q=q//List
    for j in list:
        if p%j==0 and q%j==0:
            p=p//j
            q=q//j
    print(p,q,sep='/')