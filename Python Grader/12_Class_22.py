class Card:
    def __init__(self, value, suit):
        self.value=value
        self.suit=suit

    def __str__(self):
        return '('+self.value+' '+self.suit+')'
    

    def getScore(self):
        x=['J','Q','K']
        if self.value== 'A':
            return 1
        elif self.value in x:
            return 10
        else:
            return int(self.value)

    def sum(self, other):
        return (self.getScore()+other.getScore())%10
    

    def __lt__(self, rhs):
       a=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
       b=['club','diamond','heart','spade']

       x=a.index(self.value)
       y=a.index(rhs.value)

       if x==y:
           x= b.index(self.suit)
           y= b.index(rhs.suit)

       return x<y



n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))


for i in range(n):
    print(cards[i].getScore()) #get method from the object

print("----------")

for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1])) #call function in the class
    
print("----------")

cards.sort()
for i in range(n):
    print(cards[i])