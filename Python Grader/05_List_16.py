x=int(input())

process=[x]


while True:
    if x!= 1:
     
     if x%2==0:
        x=x/2
        process.append(int(x))
     else:
        x=3*x+1
        process.append(int(x))
    
    else:
       break

process=[str(i) for i in process]

if len(process)>=15:
   print('->'.join(process[len(process)-15:]))

else:
   print('->'.join(process))




