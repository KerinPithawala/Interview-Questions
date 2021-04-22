from collections import Counter
l=list(map(int,input().split(',')))
n=len(l)
out=[]
for i in range(n):
    s=[]
    for j in range(i+1,n):
        if l[j]>l[i]:
            s.append(l[j])
    if (len(s)==0):
        out.append(-1)
    else:
        c=dict(Counter(s))
        l1=[]
        v=max(c.values())
        for i in c.keys():
            if (c[i]==v):
                l1.append(i)
        out.append(min(l1))
print(*out,sep=",")