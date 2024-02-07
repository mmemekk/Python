
data=dict()
order=[]

for i in range(int(input())):
    id,city= input().split(': ')
    data[id]=city.split(', ')
    order.append(id)

keyid=input()
keycity=data[keyid]
match=[]

for e in order:
    for i in data[e]:
        if i in keycity and e not in match and e!=keyid:
            match.append(e)

if len(match)!=0:
    print('\n'.join(match))
else:
    print('Not Found')