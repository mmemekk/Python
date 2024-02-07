filename,year=input().split()

data=[]

fn=open(filename,'r')
for i in fn :
    id,score=i.strip().split()

    if id[:2]==year[-2:]:
        data.append(float(score))

if len(data)==0:
    print('No data')
else:
    print(min(data),max(data),(sum(data)/len(data)))