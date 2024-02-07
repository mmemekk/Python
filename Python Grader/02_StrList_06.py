u=input()
v=input()

ux=u[1:-1]
vx=v[1:-1]

uy=ux.split(",")
vy=vx.split(",")

uy=[float(i) for i in uy]
vy=[float(i) for i in vy]

result1=uy[0]+vy[0]
result2=uy[1]+vy[1]
result3=uy[2]+vy[2]

final=[result1,result2,result3]
print("")
print(uy,"+",vy,"=",final)
