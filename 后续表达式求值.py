n=int(input())
for _ in range(n):
    a=list(input().split())
    stack=[]
    for i in a:
        if i.replace('.','',1).isdigit():
            stack.append(float(i))
        else:
            x=stack.pop()
            y=stack.pop()
            if i=='+':
                z=x+y
            elif i=='-':
                z=x-y
            elif i=='*':
                z=x*y
            elif i=='/':
                z=y/x
            stack.append(z)
    result="{:.2f}".format(stack[0])
    print(result)