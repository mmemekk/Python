x=int(input())


print((" ")*(x-2),"*")
for i in range(x-2):
    print(" "*(x-3-i),"*"," "*(2*i)+"*")
print("*"*(2*x-1))
    
