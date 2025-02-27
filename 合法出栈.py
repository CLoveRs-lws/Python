n=int(input())
stack=list(map(int,input().split()))
t=1
s=[]
i=0
for j in range(1,n+1):
    s.append(j)
    while s and s[-1]==stack[i] and i<n:
        s.pop()
        i+=1
if i==n:
    print("Yes")
else:
    print("No")