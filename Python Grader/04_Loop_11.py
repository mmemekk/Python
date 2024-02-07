x=input()

pchar=x[0]

count=0
result=[]

for i in range(len(x)):
    if x[i] == pchar:
        count+=1
    else:
        result.append(pchar + " " + str(count))
        pchar = x[i]
        count = 1

result.append(pchar + " " + str(count))

print(" ".join(result))
