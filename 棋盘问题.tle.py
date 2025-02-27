import math
n,k=map(int,input().split())
def f(matrix,k,n):
    count=0
    if k==0:
        return 1
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                new=[row[:] for row in matrix]
                for x in range(n):
                    new[i][x]=0
                    new[x][j]=0
                count+=f(new,k-1,n)
    return count
while n!=-1 or k!=-1:
    matrix=[]
    for i in range(n):
        str=input()
        matrix.append([])
        for j in range(n):
            if str[j]=='#':
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    print(f(matrix,k,n)//math.factorial(k))
    n,k=map(int,input().split())