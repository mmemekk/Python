d = {
'a': 2,
'b': 22,
'c': 222,
'd': 3,
'e': 33,
'f': 333,
'g': 4,
'h': 44,
'i': 444,
'j': 5,
'k': 55,
'l': 555,
'm': 6,
'n': 66,
'o': 666,
'p': 7,
'q': 77,
'r': 777,
's': 7777,
't': 8,
'u': 88,
'v': 888,
'w': 9,
'x': 99,
'y': 999,
'z': 9999,
' ': 0
}

dreverse = {}
for i in d:
    dreverse[d[i]] = i




def text2keys(text):
    result = []
    x = text.lower()
    for i in x:
      if i in d:
         result.append(str(d[i]))
    return ' '.join(result)


def keys2text(keys):
   result=[]
   y = keys.split()
   y = [int(i) for i in y]
   for i in y:
      if i in dreverse:
         result.append(dreverse[i])
   return ''.join(result)


exec(input().strip())



   