from collections import deque

# 声明方向变化的数组，代表上下左右移动
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def canVisit(x, y, n, m, maze, in_queue):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and (x, y) not in in_queue

def BFS(start, target, n, m, maze):
    q = deque([(0, start)])  # (step, (x, y))
    in_queue = {start}
    
    while q:
        step, (x, y) = q.popleft()
        
        if (x, y) == target:
            return step
        
        for i in range(MAXD):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if canVisit(next_x, next_y, n, m, maze, in_queue):
                in_queue.add((next_x, next_y))
                q.append((step + 1, (next_x, next_y)))
    
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = []
    start, target = None, None
    
    for i in range(n):
        row = input().strip()
        maze_row = []
        for j in range(m):
            if row[j] == '.':
                maze_row.append(0)
            elif row[j] == '*':
                maze_row.append(1)
            elif row[j] == 'S':
                start = (i, j)
                maze_row.append(0)
            elif row[j] == 'T':
                target = (i, j)
                maze_row.append(0)
        maze.append(maze_row)
    
    if start is None or target is None:
        print(-1)
    else:
        step = BFS(start, target, n, m, maze)
        print(step)