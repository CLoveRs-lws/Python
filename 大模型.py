class LLM:
    def __init__(self,full):
        self.full=full
        for i in range(len(full)):
            if full[i]=='-':
                mark=i
        self.name=full[:mark]
        self.size=full[mark:]
        if self.size[-1]=='B':
            self.num=1000*float(self.size[:-1])
        else:
            self.num=float(self.size[:-1])
def main():
    n=int(input())
    sum=[LLM()*n]
    for k in range(n):
        sum[k].full=input()
    sorted_LLM = sorted(LLM, key=lambda person: person.age)