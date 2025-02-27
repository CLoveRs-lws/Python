def f(n,k,matrix):
    colused=0
    def g(row,colused,placed):
        count=0
        if placed==k:
            return 1
        if row>=n:
            return 0
        count+=g(row+1,colused,placed)
        for col in range(n):
            if matrix[row][col]=='#' and not colused & (1<<col):
                count+=g(row+1,colused|(1<<col),placed+1)
        return count
    return g(0,0,0)
while True:
    n,k=map(int,input().split())
    if n==-1 and k==-1:
        break
    matrix=[]
    for _ in range(n):
        matrix.append(input())
    print(f(n,k,matrix))