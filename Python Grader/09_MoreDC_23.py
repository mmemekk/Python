data={}

def minsec(x):
    time=x.split(':')
    second=(int(time[0])*60)+int(time[1])
    return second

def secmin(x):
    time=x
    min=int(time//60)
    second=int(time-(min*60))
    if second<10:
        second='0'+str(second)
    return str(min)+':'+str(second)

for i in range(int(input())):
    song=input().split(', ')
    if song[2] not in data:
        data[song[2]]=minsec(song[3])
    else:
        data[song[2]]+=minsec(song[3])

result=sorted((data.items()), key=lambda x:x[1],reverse=True)
cutresult=result[:3]



for i in range(len(cutresult)):
    print(cutresult[i][0], '-->', secmin(cutresult[i][1]))

