# HW02 (Don't delete this line or add any line above this line.)

def read_file(filename):
    lines = []
    fn = open(filename, "r")
    for line in fn:
        lines.append(line)
    fn.close()

    for i in range(len(lines)-1):
      lines[i] = lines[i][:-1]
    
    return lines



def write_file(lines, filename):
    fout=open(filename,'w')
    for i in range(len(lines)-1):
      lines[i]=lines[i]+'\n'
    for text in lines:
      fout.write(text)
    fout.close()

def vi_editor(lines, command):
    cursorh = 0
    cursorv= 0

    insertmode = False

    line=[]
    for i in range(len(lines)):
      eachline=[]
      for k in range(len(lines[i])):
        eachline.append(lines[i][k])
      line.append(eachline)
    commands = list(command+'----')
    for i in range(len(commands)):
      if i<len(commands)-4 and ''.join(commands[i:i+5])=='[Esc]':
        commands[i:i+5]=[''.join(commands[i:i+5])]
    commands=commands[:-4]


    for e in commands:
      if e=='i'and insertmode==False:
        insertmode=True
        continue
      elif e=='[Esc]' and insertmode==True:
        insertmode=False
        continue
      
      if insertmode==False:
        if e=='j'and cursorv<len(lines)-1: #down
          cursorv+=1
        elif e=='k'and cursorv!=0: #up
          cursorv-=1
        elif e=='l' and cursorh<len(lines[cursorv])-1: #right
          cursorh+=1
        elif e=='h' and cursorh!=0: #left
          cursorh-=1
        elif e=='o': #add new line above move cursor and enter insert mode
          line.insert(cursorv,[])
          cursorh=0
          insertmode=True
          continue
        elif e=='x': #delete current character and shift inward
          if len(line[cursorv]) !=0:
            line[cursorv].pop(cursorh)
        elif e=='D': #delete that cursor postion till end and shift cursor back one unit
            line[cursorv]=line[cursorv][:cursorh]
            cursorh-=1

      if insertmode==True:
        if e=='\n':
          cursorv+=1
          cursorh=0
          line.insert(cursorv,[])
          continue

        if len(line)==0:
          line.append([])
          line[cursorv].insert(cursorh,e)
          cursorh+=1

        else:
          line[cursorv].insert(cursorh,e)
          cursorh+=1


    result=[]
    for i in range(len(line)):
      result.append(''.join(line[i]))
      
    return result

        

lines = read_file('data.txt')
commands = "lllxiThe newly added[Esc]hhhxx"
lines=vi_editor(lines, commands)
write_file(lines, 'edited_data.txt')



# lines=read_file('data.txt')


# print(vi_editor(lines,'lllxiThe newly added[Esc]hhhxx'))
