n = int(input())  # 输入数量
buffer = ''
s=0
x = {'*', '/'}
y = {'+', '-'}
for _ in range(n):
    a = input()  # 输入数学表达式
    b = []
    stack = []

    for i in a:
        if i.isdigit():
            buffer += i
        elif i == '.':
            buffer += i
            s=1
        else:
            if buffer and s:
                b.append(float(buffer))
                buffer = ''
                s=0
            elif buffer:
                b.append(int(buffer))
                buffer=''

            if stack and (i in x or i in y):
                if (i in y and stack[-1] in y) or (i in x and stack[-1] in x) or (i in y and stack[-1] in x):
                    while stack and ((i in y and stack[-1] in y) or (i in x and stack[-1] in x) or (i in y and stack[-1] in x)):
                        k = stack.pop()
                        b.append(k)
                    stack.append(i)
                elif i in x and stack[-1] in y:
                    stack.append(i)
                else:
                    stack.append(i)
            elif (i in x) or (i in y):
                stack.append(i)
            elif i == '(':
                stack.append(i)
            elif i == ')':
                t = stack.pop()
                while t != '(':
                    b.append(t)
                    t = stack.pop()
    
    if buffer and s:
        b.append(float(buffer))
        buffer = ''
        s=0
    elif buffer:
        b.append(int(buffer))
        buffer=''
    while stack:
        k = stack.pop()
        b.append(k)
    
    print(*b, sep=' ')
