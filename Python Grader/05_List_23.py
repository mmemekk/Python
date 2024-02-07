import math

x=int(input())

point=[]

for i in range(x):
    y=input().split()
    y=[float(i) for i in y ]
    distance= math.sqrt((y[0]**2 + y[1]**2))
    point.append([distance,i+1,y[0],y[1]])

point.sort(key= lambda x :x[0])

print('#'+ str(point[2][1])+':', '('+ str(point[2][2])+', '+ str(point[2][3])+')' )

