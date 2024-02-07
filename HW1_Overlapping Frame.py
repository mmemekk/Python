# HW01 (Don't delete this line or add any line above this line.)

frames = [float(x) for x in input().split()]


# write your program under this line

import math

allcommand=[]

while True:
    x=input().split()
    if x[0]=='center'or x[0]=='distance'or x[0]=='intersection'or x[0]=='union'or x[0]=='iou':
        allcommand.append(x)
    elif x [0]== "end":
        break

command=[d[0] for d in allcommand]


def pointdata(x):
    data=[frames[(x-1)*4],frames[(x-1)*4+1],frames[(x-1)*4+2],frames[(x-1)*4+3]]
    return data

def center(x,y,w,h):
    a=[ x+(w/2) , y-(h/2)]
    return a

def distance(x1,y1,x2,y2):
    dis= math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dis

def intersection(x1,y1,w1,h1,x2,y2,w2,h2):
    leftx=max(x1,x2)
    rightx=min((x1+w1),(x2+w2))
    topy=min(y1,y2)
    bottomy=max((y1-h1),(y2-h2))

    width=rightx-leftx
    height=topy-bottomy

    if width<0 or height<0:
        area=0
    else:
        area=width*height
    
    return float(area)

def union(x1,y1,w1,h1,x2,y2,w2,h2):
    intersectarea= intersection(x1,y1,w1,h1,x2,y2,w2,h2)
    allarea=(w1*h1)+(w2*h2)
    unionarea=allarea-intersectarea

    return unionarea

def iou(x1,y1,w1,h1,x2,y2,w2,h2):
    a=intersection(x1,y1,w1,h1,x2,y2,w2,h2)
    b=union(x1,y1,w1,h1,x2,y2,w2,h2)

    ratio=a/b

    return ratio



cal=[]

for i in range(len(command)) :
    if command[i]=='center':
        f= int(allcommand[i][1])
        info=pointdata(f)
        centroid=center(info[0],info[1],info[2],info[3])
        cal.append('('+str(centroid[0])+','+str(centroid[1])+')')

    elif command[i]=='distance':
        f= [int(allcommand[i][1]), int(allcommand[i][2])]
        info1=pointdata(f[0])
        info2=pointdata(f[1])

        cen1= center(info1[0],info1[1],info1[2],info1[3])
        cen2= center(info2[0],info2[1],info2[2],info2[3])
        cal.append(distance(cen1[0],cen1[1],cen2[0],cen2[1]))

    elif command[i]=='intersection':
        f= [int(allcommand[i][1]), int(allcommand[i][2])]
        coor1=pointdata(f[0])
        coor2=pointdata(f[1])
        cal.append(intersection(coor1[0],coor1[1],coor1[2],coor1[3],coor2[0],coor2[1],coor2[2],coor2[3]))

    elif command[i]=='union':
        f= [int(allcommand[i][1]), int(allcommand[i][2])]
        coor1=pointdata(f[0])
        coor2=pointdata(f[1])
        cal.append(union(coor1[0],coor1[1],coor1[2],coor1[3],coor2[0],coor2[1],coor2[2],coor2[3]))

    elif command[i]=='iou':
        f= [int(allcommand[i][1]), int(allcommand[i][2])]
        coor1=pointdata(f[0])
        coor2=pointdata(f[1])
        cal.append(iou(coor1[0],coor1[1],coor1[2],coor1[3],coor2[0],coor2[1],coor2[2],coor2[3]))


for i in cal:
    print(i)



