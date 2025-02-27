n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=[]
i=0
j=0
for _ in range(2*n):
    if i<n and j<n:
        if a[i]<=b[j]:
            ans.append(a[i])
            i+=1
        else:
            ans.append(b[j])
            j+=1
    elif i>=n:
        ans.append(b[j])
        j+=1
    else:
        ans.append(a[i])
        i+=1
print(*ans,sep=' ')
