x=int(input())

name=[["Robert","Dick"],["William","Bill"],["James","Jim"],["John","Jack"],["Margaret","Peggy"],["Edward","Ed"],
["Sarah","Sally"],["Andrew","Andy"],["Anthony","Tony"],["Deborah","Debbie"]]

first=[d[0] for d in name]
nickname=[d[1] for d in name]

y=[]
z=[]

for i in range(x):
    y.append(input())

for i in range(len(y)):
    if y[i] in first:
        a=first.index(y[i])
        z.append(nickname[a])
    
    elif y[i] in nickname:
        b=nickname.index(y[i])
        z.append(first[b])
    else:
        z.append("Not found")
        

print('\n'.join(z))