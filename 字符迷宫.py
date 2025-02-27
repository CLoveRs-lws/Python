from collections import deque
n, m = map(int, input().split())
maze = [input() for _ in range(n)]
count = [[-1]*m for _ in range(n)]
direction=[(0,1),(1,0),(-1,0),(0,-1)]
for p in range(n):
    for q in range(m):
        if maze[p][q]=='S':
            start=(p,q)
        if maze[p][q]=='T':
            end=(p,q)
queue=deque([start])
count[start[0]][start[1]]=0
def effective(x,y):
    return -1<x<n and -1<y<m and (maze[x][y]=='.' or maze[x][y]=='T') and count[x][y]==-1
step=0
while queue and count[end[0]][end[1]]==-1:
    size=len(queue)
    step+=1
    for _ in range(size):
        x,y=queue.popleft()
        for i, j in direction:
            xx, yy=x+i, y+j
            if effective(xx,yy):
                count[xx][yy]=count[x][y]+1
                queue.append((xx,yy))
print(count[end[0]][end[1]])