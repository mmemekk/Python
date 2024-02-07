import math 

def distance1 (x1,y1,x2,y2):
    d=math.sqrt((x1-x2)**2 + (y1-y2)**2)

    return d

def distance2(p1,p2):
    a,b=p1
    c,d=p2
    d=math.sqrt((a-c)**2 + (b-d)**2)
    return d

def distance3(c1,c2):
    x1,y1,r1=c1
    x2,y2,r2=c2
    d=distance1(x1,y1,x2,y2)
    
    if d > (r1+r2):
        overlap=False
    else:
        overlap=True

    return d,overlap

def perimeter(points):
    d = 0
    for i in range(len(points)-1):
        d += distance2(points[i],points[i+1])
    d += distance2(points[-1],points[0])
    return d

    
exec(input().strip())


