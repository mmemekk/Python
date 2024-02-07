
id=[]
gradestu=[]
grade=['F','D','D+','C','C+','B','B+','A','A']

while True:
    x=input()
    if x== 'q':
        break
    else:
        y=x.split()
        id.append(y[0])
        gradestu.append(y[1])

uid=input().split()

for i in range(len(uid)):
    ind=id.index(uid[i])
    currentgrade=gradestu[ind]
    gradeindex=grade.index(currentgrade)
    gradestu[ind]=grade[gradeindex+1]


id=[int(i) for i in id]

sortid=sorted(id)

sortgradestu=[]

for i in range(len(id)):
    ind=id.index(sortid[i])
    sortgradestu.append(gradestu[ind])


for i in range(len(sortid)):
    print(sortid[i], sortgradestu[i])





