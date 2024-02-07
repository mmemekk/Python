numline=int(input())

first=[]
for i in range(numline):
    first.append(int(input()))

second=input().split()
second=[int(i) for i in second]

third=[]

while True:
    x=int(input())
    if x== -1:
        break
    else:
        third.append(x)

data=first+second+third

output=[]

for i in range(len(data)):
    if i%2==0:
        output.append(data[i])
    else:
        output.insert(0,data[i])

print(output)

