x=input().lower()
y=input().lower()

x=x.replace(' ','')
y=y.replace(' ','')
a=list(x)
b=list(y)

a.sort()
b.sort()


if a==b:
    print ("YES")
else:
    print ("NO")