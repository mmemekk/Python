x=input()
code=["06","08","09"]
y=x[:2]

if y in code and len(x)==10:
    print ("Mobile number")

else:
    print ("Not a mobile number")