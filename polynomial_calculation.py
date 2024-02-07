x=[(1,0),(1, 25), (1, 50), (1, 75)]
y=[(1, 0), (1, 5), (2, 10), (2, 15), (2, 20), (2, 25), (2, 30), (2, 35), (1, 40), (1, 45)]

result = []

for i in range(len(x)):
    for j in range(len(y)):
        result.append((x[i][0]*y[j][0],x[i][1]+y[j][1]))

final=dict()

for i in range(len(result)):
    if result[i][1] not in final:
        final[result[i][1]]=result[i][0]
    else:
        final[result[i][1]]+=result[i][0]

finaltuple =[(v, k) for k, v in final.items()]

sortanswer = sorted(finaltuple, key=lambda x: x[1])


print(sortanswer)
