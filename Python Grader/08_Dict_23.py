x=int(input())
directory={}

for i in range(x):
    a,b,phone=input().split()
    name=a+' '+b
    directory[name]=phone

directoryreverse={}

for i in directory:
    directoryreverse[directory[i]]=i

y=int(input())

for i in range(y):
    z=input()
    if z in directory:
        print(z ,"-->", directory[z])
    elif z in directoryreverse:
        print(z ,"-->", directoryreverse[z])
    else:
        print(z ,"-->", "Not found")
