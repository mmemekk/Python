x=list(input())
y=["0","1","2","3","4","5","6","7","8","9"]

for i in range(len(x)):
    if x[i] in y:
        y.remove(x[i])


if len(y)==0:
    print("None")
else:
    print(','.join(y))

