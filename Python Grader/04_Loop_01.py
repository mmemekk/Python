total=0
n=0

while True:
    x=input()
    if x=="q":
        break
    else:
         total+=float(x)
    n+=1

if n==0:
    print ("No Data")
else:
    print (round(total/n,2))
