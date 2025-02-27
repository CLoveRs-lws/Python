str=[]
while True:
    try:
        str=input()
        L=len(str)
        stack=[]
        l=0
        setl=[]
        setr=[]
        for i in range(L):
            if str[i]=='(':
                stack.append(str[i])
                setl.append(i)
            elif str[i]==')'and len(setl)>=1:
                stack.pop()
                setl.pop()
            elif str[i]==')':
                setr.append(i)
        print(str)
        for j in range(L):
                if j in setl:
                    print('$',end='')
                elif j in setr:
                    print('?',end='')
                else:
                    print(' ',end='')
        print()
    except EOFError:
        break