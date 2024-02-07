x=int(input())

y=""
z=""

if x>0:
    y="positive"
elif x==0:
    y="zero"
else:
    y="negative"

if x%2==0:
    z="even"
else: 
    z="odd"

print(y)
print(z)