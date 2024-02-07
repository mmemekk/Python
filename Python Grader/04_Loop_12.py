num=int(input())

zig=[]
zag=[]

for i in range(num):
    x=input().split()
    if i%2==0:
        zig.append(int(x[0]))
        zag.append(int(x[1]))
    else:
        zig.append(int(x[1]))
        zag.append(int(x[0]))

command=input()

if command=="Zig-Zag":
    print(min(zig),max(zag))
else:
    print(min(zag),max(zig))
