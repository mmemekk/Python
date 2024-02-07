winner=set()
loser=set()

for i in range(int(input())):
    team=input().split()
    winner.add(team[0])
    loser.add(team[1])


for e in list(loser):
    if e in winner:
        winner.remove(e)

print(sorted(winner))