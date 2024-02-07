n=int(input())

data=[]

for i in range(n):
    data.append(input().split())

data.sort()

filter=input().split()

index={}

for i in range(len(filter)):
    for j in range(len(data)):
        for k in range(len(data[j])):
            if data[j][k]==filter[i] and k!=0:
                if j not in index:
                    index[j]=1
                else:
                    index[j]+=1

result=[]

for i in index:
    if index[i]==len(filter):
        result.append(i)

if len(result)==0:
    print('Not Found')
else:
    result.sort()
    for i in result:
        print((' ').join(data[i]))

        
    



