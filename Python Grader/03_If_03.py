x=input()
y=x.split()
z=[float(i) for i in y]
max=0 
min=0

if z[0]>=z[1] and z[0]>=z[2] and z[0]>=z[3]:
    max= z[0]
elif z[1]>=z[0] and z[1]>=z[2] and z[1]>=z[3]:
    max= z[1]
elif z[2]>=z[0] and z[2]>=z[1] and z[2]>=z[3]:
    max= z[2]
elif z[3]>=z[0] and z[3]>=z[1] and z[3]>=z[2]:
    max= z[3]

if z[0]<=z[1] and z[0]<=z[2] and z[0]<=z[3]:
    min= z[0]
elif z[1]<=z[0] and z[1]<=z[2] and z[1]<=z[3]:
    min= z[1]
elif z[2]<=z[0] and z[2]<=z[1] and z[2]<=z[3]:
    min= z[2]
elif z[3]<=z[0] and z[3]<=z[1] and z[3]<=z[2]:
    min= z[3]

z.remove(max)
z.remove(min)

print (round((z[0]+z[1])/2,2))