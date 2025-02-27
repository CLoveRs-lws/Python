n=int(input())
answer=[]
if n==0:
    print(0)
while n>0:
    a=n%8
    answer.append(a)
    n=n//8
l=len(answer)
for i in range(l):
    print(answer[l-1-i],end='')