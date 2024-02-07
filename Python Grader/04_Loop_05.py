x=input()
y=input()
z=0

chremove=['"',"(",")",",",".","'"]
for ch in chremove:
    y=y.replace(ch," ")

y=y.split()

for i in y:
    if i==x:
        z+=1

print(z)

