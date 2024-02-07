x=input()
y=list(x)

if x=="no parentheses":
    print("no parentheses")
else:
    for i in range(len(x)):
        if y[i]=="(":
            y[i]=("[")
        elif y[i]=="[":
            y[i]=("(")
        elif y[i]==")":
            y[i]=("]")
        elif y[i]=="]":
            y[i]=(")")
    print("".join(y))


#it can be done by using replace()
