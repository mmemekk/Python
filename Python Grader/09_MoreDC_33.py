def add_poly(c,d):

    a=list(c)
    b=list(d)
    order=[a[i][1] for i in range(len(a))]
    for i in range(len(b)):
        if b[i][1] in order: 
            position=order.index(b[i][1])
            coef1=int(a[position][0])
            coef2=int(b[i][0])
            sum=coef1+coef2
            a.pop(position)
            if sum==0:
                order.pop(position)
                continue
            else:
                result=(coef1+coef2,b[i][1])
                a.insert(position,result)
        else:
            a.append(b[i])

    a.sort(key= lambda x: x[1], reverse=True)
    return a

def mult_poly(p1,p2):

    a=list(p1)
    b=list(p2)

    if len(a)==0 or len(b)==0:
        return []

    acoeff=[a[i][0] for i in range(len(a))]
    bcoeff=[b[i][0] for i in range(len(b))]
    adeg=[a[i][1] for i in range(len(a))]
    bdeg=[b[i][1] for i in range(len(b))]

    data=[]
    for i in range(len(a)):
        multiply=[]
        for j in range(len(b)):
            multcoef=acoeff[i]*bcoeff[j]
            multdeg=adeg[i]+bdeg[j]
            multiply.append((multcoef,multdeg))
        
        data.append(multiply)

    result=data[0]

    for i in range(1,len(data)):
        result=add_poly(result,data[i])


    return result


# p1=[(3,6),(2,4)]
# p2=[(1,4),(-1,2)]
# print(mult_poly(p1,p2))

for i in range(3):
    exec(input().strip())