x=input()

a=x[3::7]
b=x[7::5]
c=int(a)+int(b)+10000
d=str(c)[-4:-1]
t=list(d)
t=[int(i) for i in t]
e=sum(t)
e2=str(e)[:-2:-1]
e3=int(e2)+1
alphabets=['A','B','C','D','E','F','G','H','I','J']
f=alphabets[e3-1]

secret=(d+f)
print(secret)

