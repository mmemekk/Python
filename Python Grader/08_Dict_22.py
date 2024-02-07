n=int(input())
icecream={}

for i in range(n):
    a,b=input().split()
    icecream[a]=float(b)

s=int(input())

sale={}

for i in range(s):
    c,d =input().split()
    if c in icecream and c not in sale:
        sale[c]=icecream[c]*int(d)
    elif c in icecream and c in sale:
        sale[c]+=icecream[c]*int(d)

totalsale=0

for i in sale:
    totalsale+=sale[i]



output=[]

if len(sale)==0:
    print('No ice cream sales')
else:
    maxsale=max(sale.values())
    for i in sale:
        if sale[i]==maxsale:
            output.append(i)

    print("Total ice cream sales:", totalsale)
    print("Top sales:", ', '.join(sorted(output)))

