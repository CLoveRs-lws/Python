dic = {}
s = input()
l = len(s)
for i in range(l):
    if s[i] not in dic:
        dic[s[i]] = 1
    else:
        dic[s[i]] += 1
for j in range(l):
    if dic[s[j]]==1:
        print(j)
        break
else:
    print(-1)