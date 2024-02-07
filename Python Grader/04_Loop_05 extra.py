x=input()
y=input()
a=0
z=0
for i in range(len(y)):
    z=0
    if y[i]==x[0]:
        for k in range(len(x)):
            if y[i+k]!=x[k]:
                z=0
                break
            else:
                z+=1
        z=z/len(x)
    a+=z

print(int(a))