"""
                                       * Batthele Ship *
                                Created by MAEDHUS and NADON 512
"""
#Print out intro message
print("\n")
print("          *** WELCOME TO BATTLE SHIP ***")
print("_____________________________________________________")
print("*This game requires two player: Player A and Player B")
print()
print("*Player ""A"" will place 3 small ships and 2 large ships")
print()
print("*Player ""B"" will guess the ship")
print("_____________________________________________________")
print()
print("        ***IF YOU'RE READY, LET'S START!!!***")
print("\n")
##########################
import string
alphabet=[] #create list for alphabets for board usage
for i in range(65,75): #Range for Uppercase Alphabets
    alphabet.append(chr(i)) #Store in list

alphabetlower=[]#create list for alphabets(lowercase) for board usage
for i in range(97,107):#Range for Lowercase Alphabets
    alphabetlower.append(chr(i)) #Store in list

boardlist=[] #Create list for board to store

class printing: #create board class
    def __init__(self,row,column): #allow input for number of rows and columns
        self.row=row 
        self.column=column

    def array(self): #printing board function
        for x in range(self.column): #store column first
            boardlist.append(["-"]*self.column)
        print("   "+"  ".join(str(x) for x in range (1,self.column+1))) #print column header
        for r in range(self.row): # print row header and organize to row
            print(alphabet[0+r]+"  " +"  ".join(str(c) for c in boardlist[r]))
        
board=printing(10,10)
board.array() #create the board

conversion = {"A": 1, "B": 2, "C": 3,"D": 4,"E": 5,"F": 6,"G": 7, #Dictionary convert alphabet to value
              "H": 8, "I": 9,"J": 10,"a": 1, "b": 2, "c": 3,"d": 4,
              "e": 5,"f": 6,"g": 7,"h": 8, "i": 9,"j": 10}

#############################
position=[] #create list for location
class Ship:
    def __init__(self,threeunits,fourunits):
        self.threeunits=threeunits
        self.fourunits=fourunits
    def message(self): #print message
        print()
        print("PLAYER A: PLACE THE SHIPS")

    def locatingship(self):
        smallship=0 #set up variable for counting
        bigship=0
        while smallship < self.threeunits: #placing smallship
            try:
                print("SMALL SHIP TO PLACE:", self.threeunits-smallship) #tell how many ship left to place
                column= int(input("Select Column (1-10):")) #enter row
                row= str(input("Select Row(A-J):")) #enter column
                direction =str(input("Direction (h for horizontail, v for vertical):")) #enter direction
                
                if column >10 or column <0: #if the player place out of column
                    print("Column not existed!, Please Try Again...")
                    print()
                    continue
                elif row not in alphabet and row not in alphabetlower: #if the player input wrong row
                    print("Row not existed!, Please Try Again...")
                    print()
                    continue
                elif direction != "h" and direction!= "v": #if the player input wrong direction
                    print("Please input a correct direction!, Try Again...")
                    print()
                    continue
                else:
                    
                    if direction=="h": #for horizontal place
                        rows = conversion[row] #convert alphabet to value
                        shiph1=(rows-1, column-1) #store location to variable
                        shiph2=(rows-1, column)
                        shiph3=(rows-1, column+1)                    
                        if shiph1 in position or shiph2 in position or shiph3 in position: #check if the ship already place or not
                            print("The place already have a boat!, Please Try Again...")
                            continue
                        else:
                            position.append(shiph1) #append the location of the ship to the created list
                            position.append(shiph2)
                            position.append(shiph3)
                            boardlist[rows-1][column+1]="X" #Append the ship's postition in board list 
                            boardlist[rows-1][column]="X"
                            boardlist[rows-1][column-1]="X"
                            board.array() #print board to show the ship that is placed
                            smallship+=1 #count the ship that is placed
                  
                    if direction=="v":#for vertical place
                        rows = conversion[row]#convert alphabet to value
                        shipv1=(rows-1, column-1)#store location to variable
                        shipv2=(rows, column-1)
                        shipv3=(rows+1, column-1)                    
                        if shipv1 in position or shipv2 in position or shipv3 in position:#check if the ship already place or not
                            print("The place already have a boat!, Please Try Again...")
                            continue
                        else:
                            position.append(shipv1)#append the location of the ship to the created list
                            position.append(shipv2)
                            position.append(shipv3)
                            boardlist[rows+1][column-1]="X"#Append the ship's postition in board list
                            boardlist[rows][column-1]="X"
                            boardlist[rows-1][column-1]="X"
                            board.array() #print board to show the ship that is placed
                            smallship+=1 #count the ship that is placed
            except ValueError: #for wrong input of the column
                print("Please insert a number")
            
            except IndexError: #in case if the player place the ship out of board
                print("The ship is out of board!, Try Again!")
                continue
            
        while bigship < self.fourunits: #placing big ships
            try:
                print("LARGE SHIP TO PLACE:",self.fourunits-bigship ) #tell how many ship left to place
                column= int(input("Select Column (1-10):")) #input column
                row= str(input("Select Row(A-J):")) #input row
                direction =str(input("Direction (h for horizontail, v for vertical):")) #input direction
                
                if column >10 or column <0: #if the player place out of column
                    print("Column not existed!, Please Try Again...")
                    print()
                    continue
                elif row not in alphabet and row not in alphabetlower: #if the player input wrong row
                    print("Row not existed!, Please Try Again...")
                    print()
                    continue
                elif direction != "h" and direction!= "v": #if the player input the wrong direction
                    print("Please input a correct direction(h/v)!, Try Again...")
                    print()
                    continue
                else:
                    
                    if direction=="h": #for horizontal place
                        rows = conversion[row] #convert alphabet to value
                        shiph1=(rows-1, column-1) #store location to variable
                        shiph2=(rows-1, column)
                        shiph3=(rows-1, column+1)
                        shiph4=(rows-1, column+2)
                        if shiph1 in position or shiph2 in position or shiph3 in position or shiph4 in position: #check if the ship already place or not
                            print("The place already have a boat!, Please Try Again...")
                            continue
                        else:
                            position.append(shiph1) #append the location of the ship to the position list
                            position.append(shiph2)
                            position.append(shiph3)
                            position.append(shiph4)
                            boardlist[rows-1][column+2]="X" #Append the ship's postition in board list
                            boardlist[rows-1][column+1]="X"
                            boardlist[rows-1][column]="X"
                            boardlist[rows-1][column-1]="X"
                            board.array() #print board out to show the placed position
                            bigship+=1 #count for ship placement
                  
                    if direction=="v": #for verical place
                        rows = conversion[row]#convert alphabet to value
                        shipv1=(rows-1, column-1) #store location to variable
                        shipv2=(rows, column-1)
                        shipv3=(rows+1, column-1)
                        shipv4=(rows+2, column-1)
                        if shipv1 in position or shipv2 in position or shipv3 in position or shipv4 in position:#check if the ship already place or not
                            print("The place already have a boat!, Please Try Again...")
                            continue
                        else:
                            position.append(shipv1) #append the location of the ship to the position list
                            position.append(shipv2)
                            position.append(shipv3)
                            position.append(shipv4)
                            boardlist[rows+2][column-1]="X" #Append the ship's postition in board list
                            boardlist[rows+1][column-1]="X"
                            boardlist[rows][column-1]="X"
                            boardlist[rows-1][column-1]="X"
                            board.array() #print board out to show the placed position
                            bigship+=1 #count for ship placement
            except ValueError: #for wrong input of the column
                print("Please insert a number")
            
            except IndexError:#in case if the player place the ship out of board
                print("The ship is out of board!, Try Again!")
                continue

Placing_ship= Ship(2, 3) #Created number of small and big ship
Placing_ship.message() #call message function in class
Placing_ship.locatingship() #call locating ship function

####################################
guess=[] #create guess list
class Shot: #create class for shot
    def __init__(self, turn):
        self.turn =turn
    
    def message(self): #print out message 
        print("\n\n\n\n\n\n")

        print("***NOW IT'S PLAYER B TO GUESS***")
        input("Press Enter to Continue:")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
    def guessing(self): #guessing function
        playturn=0
        Totalship=len(position) 
        while playturn<self.turn: #allow player to guess if the turns are left
            try:
                print("TURN LEFT:", self.turn-playturn) #Indicate how many turn left
                guesscolumn=int(input("Guess Column(1-10):")) #guess column
                guessrow=str(input("Guess Row(A-J):")) #guess row

                if guesscolumn >10 or guesscolumn <0: #for invalid column
                    print("Column not existed!, Please Try Again...")
                    print()
                    continue
                elif guessrow not in alphabet and guessrow not in alphabetlower: #for invalid row
                    print("Row not existed!, Please Try Again...")
                    print()
                    continue
                else:
                    guessrows = conversion[guessrow] #convert the alphavet to value
                    guesspoint=(guessrows-1, guesscolumn-1) #append the guess point to the variable
               
                if guesspoint in guess: #check if the point is already guess or not
                    print("This point is aleady guessed, please try again")
                    print()
                    continue
                
                else:
                    if guesspoint in position: # if the guess point is in the ship's location (HIT)
                        guess.append(guesspoint) #append to the list to record that this point is already guess
                        boardlist[guessrows-1][guesscolumn-1]="X" #append position in board list to be X
                        board.array() #pring board
                        print("\n")
                        print("*YOU HIT!!!*") 
                        print("\n")
                        playturn+=1
                        Totalship-=1
                    else: # if the guess point is not in the ship's location (MISSED)
                        guess.append(guesspoint)#append to the list to record that this point is already guess
                        boardlist[guessrows-1][guesscolumn-1]="O"#append position in board list to be O
                        board.array() #print board
                        print("\n")
                        print("*YOU MISSED!*")
                        print("\n")
                        playturn+=1
                        
                if Totalship==0: # if all the ships are sunk, print Win Message and end the loop
                    print("______________________________")
                    print("***CONGRATULATION YOU WIN!!!***")
                    break
                
            except ValueError: #for worng in put column
                print("Please insert a number!")
            
        if playturn==self. turn: # if the turn ran out, print loose message
            print("______________________________")
            print("**YOU LOSE!**")
            print("OUT OF TURN!!")
Shotting=Shot(35) #input number of turn that is allowed
Shotting.message() #call message function
boardlist.clear() #clear the board list for guessing
board.array() #print the cleared board
Shotting.guessing() #call guessing function







