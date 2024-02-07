n=int(input())

amount={}



for i in range(n):
    dept,num=input().split()
    amount[dept]=int(num)

m=int(input())
stu=[]
for i in range(m):
    x=input().split()
    x[1]=float(x[1])
    stu.append(x)

stu.sort(key=lambda x: x[1], reverse=True)

result=[]
for i in range(len(stu)):
    for j in range(2,len(stu[i])):
        if amount[stu[i][j]]!=0:
            amount[stu[i][j]]-=1
            result.append([stu[i][0],stu[i][j]])
            break

result.sort()

for i in range(len(result)):
    print(' '.join(result[i]))