class Card:

    def __init__(self, value, suit):
        self.value=value
        self.suit=suit

    def __str__(self):
        return '('+self.value+' '+self.suit+')'


    def next1(self):
        a=['3','4','5','6','7','8','9','10','J','Q','K','A','2','3']
        b=['club','diamond','heart','spade','club']

        x=a.index(self.value)
        y=b.index(self.suit)

        if y==3:
            x+=1

        return Card(a[x],b[y+1])
    
    def next2(self):
        a=Card.next1(self)
        self.value=a.value
        self.suit=a.suit




n = int(input())
cards = []

for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].next1())

print("----------")

for i in range(n):
    print(cards[i])

print("----------")

for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
