def total(pocket):
    sum=0
    for i in pocket:
        sum+=(i*pocket[i])

    return sum 

def take(pocket,money_in):
    for i in money_in:
        if i in pocket:
            pocket[i]+=money_in[i]
        else:
            pocket[i]=money_in[i]

    return pocket

def pay(pocket,amt):
    sum=total(pocket)
    money={}
    if sum<amt:
        return dict()
    else:
        for i in pocket:
            if i<amt:
                amount=amt//i
                if amount<=pocket[i]:
                    pocket[i]-=amount
                    amt-=(amount*i)
                    money[i]=amount
                else:
                    amt-=(pocket[i]*i)
                    money[i]=pocket[i]
                    pocket[i]=0

    x=list(money.items())
    print('Thisis',x)


    return money





exec(input().strip())