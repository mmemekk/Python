x=input().lower()
d={}
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in x:
    if i not in d and i in alphabet:
        d[i]=1
    elif i in alphabet:
        d[i]+=1
a=[]
for i in d:
    a.append([int(-d[i]),i])
a.sort()

for i in range(len(a)):
    print(a[i][1],"->", -a[i][0])


#consider negative value because we want order frequency from large to small
#but the alphabet order from small to large
