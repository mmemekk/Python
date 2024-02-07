data=dict()
typeorder=[]

while True:
    x=input()
    if x=='q':
        break

    name,type =x.split(', ')

    if type not in typeorder:
        typeorder.append(type)

    if type in data:
        data[type].append(name)
    else:
        data[type]=[name]


for e in typeorder:
    print(e+':', ', '.join(data[e]))