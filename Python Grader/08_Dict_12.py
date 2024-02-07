x=int(input())
d={}

for i in range(x):
    a,b=input().split()
    d[a]=b


r={}
for i in d:
    r[d[i]]=i

y=int(input())
v=[]
for i in range(y):
    z=input()
    if z in d:
        v.append(d[z])
    elif z in r:
        v.append(r[z])
    else:
        v.append("Not found")

for i in v:
    print(i)