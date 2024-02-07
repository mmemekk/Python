n=int(input())

if n<1000:
    print(n)

elif n>=1000 and n<10000:
    print(str(round(n/1000,1))+"K")
elif n>=10000 and n<1000000:
    print(str(int(round(n/1000,0)))+"K")

elif n>=1000000 and n<10000000:
    print(str(round(n/1000000,1))+"M")
elif n>=10000000 and n<1000000000:
    print(str(int(round(n/1000000,0)))+"M")

elif n>=1000000000 and n<10000000000:
    print(str(round(n/1000000000,1))+"B")
elif n>=10000000000:
    print(str(int(round(n/1000000000,0)))+"B")