n,m=map(int,input().split())
matrix=[]
count=[]
def bfs(matrix):
    cur=[0]
    while(len(cur)!=0):
        curr=cur.copy()
        cur=[]
        for k in curr:
            j=k%m
            i=(k-j)//m
            if -1<j+1<m and count[i][j+1]==-1 and matrix[i][j+1]==0:
                count[i][j+1]=count[i][j]+1
                cur.append(i*m+j+1)
            if -1<i+1<n and count[i+1][j]==-1 and matrix[i+1][j]==0:
                count[i+1][j]=count[i][j]+1
                cur.append((i+1)*m+j)
            if -1<j-1<m and count[i][j-1]==-1 and matrix[i][j-1]==0:
                count[i][j-1]=count[i][j]+1
                cur.append(i*m+j-1)
            if -1<i-1<n and count[i-1][j]==-1 and matrix[i-1][j]==0:
                count[i-1][j]=count[i][j]+1
                cur.append((i-1)*m+j)

for i in range(n):
    matrix.append(list(map(int,input().split())))
    tool=[]
    for j in range(m):
        tool.append(-1)
    count.append(tool)
if matrix[0][0]==0:
    count[0][0]=0
    bfs(matrix)
print(count[n-1][m-1])