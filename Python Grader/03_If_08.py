d=int(input())
m=int(input())
y=int(input())-543

a=[1,2,3,4,5,6,7,8,9,10,11,12]
b=[31,28,31,30,31,30,31,31,30,31,30,31]

result=d+sum(b[:m-1])

if (y%400==0 or (y%4==0 and y%100!=0))  and m>2:
    result+=1

print (result)