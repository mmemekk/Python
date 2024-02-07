x=[int(i) for i in input().split()]
x.sort()

value=[]

check='h'

for i in range(len(x)):
    if x[i] != check:
        value.append(x[i])
        check=x[i]

count=len(value)

if count>10:
    value=value[:10]

print(count)
print(value)
