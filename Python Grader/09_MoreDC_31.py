def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def is_coprime(a,b,c):
    if gcd(a,b)==1:
        return True
    if gcd(a,c)==1:
        return True
    if gcd(b,c)==1:
        return True

    return False

def primitive_Pythagorean_triples(max_len):
    triple=[]
    for c in range(max_len+1):
        for b in range(c):
            for a in range(b):
                if (a**2)+(b**2)==(c**2) and is_coprime(a,b,c)==True:
                    triple.append([a,b,c])


    triple.sort(key=lambda x:(x[2],x[0]))

    return triple

exec(input().strip())


