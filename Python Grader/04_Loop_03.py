x=input()
y=input()
k=0

if len(x) != len(y):
    print ("Incomplete answer")
else:
    for i in range(len(x)):
        if x[i] == y[i]:
         k+=1

    print(k)
    



