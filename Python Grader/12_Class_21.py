class Complex:
    def __init__(self,real,im):
        self.real=real
        self.im=im

    def __str__(self): #chane object to string
        if self.real==0:
            if self.im==0:
                return '0'
            if self.im==1:
                return 'i'
            if self.im==-1:
                return '-i'
            return str(self.im)+'i'
        
        if self.im==0:
            return str(self.real)
        if self.im<-1:
            return str(self.real)+str(self.im)+'i'
        if self.im==1:
            return str(self.real)+'+'+ 'i'
        if self.im==-1:
            return str(self.real)+'-'+ 'i'
        
        return str(self.real)+'+'+str(self.im)+'i'
    
    def __add__(self,rhs):
        return Complex(self.real+rhs.real,self.im+rhs.im)
    
    def __mul__ (self,rhs):
        return Complex((self.real*rhs.real)-(self.im*rhs.im),(self.real*rhs.im+self.im*rhs.real))
    
    def __truediv__ (self,rhs):
        rpart=((self.real*rhs.real)+(self.im*rhs.im))/(rhs.real**2+rhs.im**2)
        ipart=((-self.real*rhs.im)+(self.im*rhs.real))/(rhs.real**2+rhs.im**2)
        return Complex(rpart,ipart)


t,a,b,c,d=[int(x) for x in input().split()]
c1=Complex(a,b)
c2=Complex(c,d)

if t==1:print(c1)
elif t==2: print(c2)
elif t==3: print(c1+c2)
elif t==4: print(c1*c2)
else: print(c1/c2)