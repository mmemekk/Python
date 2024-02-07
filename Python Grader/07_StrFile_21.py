a1=['a','b','c','d','e','f','g','h','i','j','k','l','m']
a2=['n','o','p','q','r','s','t','u','v','w','x','y','z']

a1upper=[i.upper() for i in a1]
a2upper=[i.upper() for i in a2]

def rot13(text):
    newtext=''
    for i in range(len(text)):
        if text[i] in a1:
            ind=a1.index(text[i])
            newtext+=a2[ind]
        elif text[i] in a1upper:
            ind=a1upper.index(text[i])
            newtext+=a2upper[ind]
        elif text[i] in a2:
            ind=a2.index(text[i])
            newtext+=a1[ind]
        elif text[i] in a2upper:
            ind=a2upper.index(text[i])
            newtext+=a1upper[ind]
        else:
            newtext+=text[i]      

    return newtext

x=input()
while x != 'end':
    print(rot13(x))
    x=input()

