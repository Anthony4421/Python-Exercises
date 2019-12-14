import random

'''
Generates a 12 x 12 wordsearch grid placing the words either horizontally, vertically or diagonally
depending on what the user specifies. There are 10 words in a word list that are randomly
placed in the wordsearch in the direction specified by the user
'''

def welcome():

 print("Welcome to the Wordearch Generator.")
 
def select_direction():
 direction = input("Please select the direction you would like words to be placed - (H) - Horizontally (V) - Vertically (D) - Diagonally: ")
 direction = direction.upper()
 
 return direction
 
 
def initialise_grid():

#Initialises the grid
 
 gridletters = [['1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1'],
		['1','1','1','1','1','1','1','1','1','1','1','1','1'],
		['1','1','1','1','1','1','1','1','1','1','1','1','1'],
		['1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1']]

                       

 return(gridletters)

def generate_grid(gridletters):

#Generates random letters in the grid
#in postions not taken by the words

 all_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
 
 for x in range(0,len(gridletters)):
  for y in range(0,len(gridletters[x])):
   if gridletters[x][y] == '1':
    letters = random.choice(all_letters)
    gridletters[x][y] = letters        

 return(gridletters)

def print_gridletters(gridletters):

#Prints the grid
    
 for x in range(0,len(gridletters)):
  print(gridletters[x])

def generate_wordlist():

#list to place all words to be places in the wordearch grid
 wordlist = ['MAGIC', 'GADGET', 'BEER', 'MONEY', 'PHONE', 'PYTHON', 'VISUAL', 'PROGRAM', 'SPORT']

 return(wordlist)


def print_wordlist(gridletters, wordlist):
#Prints the list of words generated for the game
 print("\n",end="")
 for x in range(0,len(wordlist)):
  print(wordlist[x])


def place_word_horizontally(wordlist, gridletters):
#Places the generated words random positions in the grid
#Ensures words do not overlap in the grid

 for x in range(0,len(wordlist)):
  #Generates horizontal position. Start position is 0 and max position is length of gridletters grid minus 1
  #We are using minus 1 because we are starting the position of 0 as opposed to 1
  hpos = random.randint(0,len(gridletters)-1)
  
  #Generates vertical position. Start position is 0 and max position is length of gridletters in the row minus the
  #length of the current word
  vpos = random.randint(0,len(gridletters[x])-len(wordlist[x]))
  
  #Total is the end position of the range we expect to see 1's when checking words do not overlap
  total = vpos + (len(wordlist[x]))
  
  
  #While there are not all 1's (blanks) from [horizontal position][vertical position:total position number in row]
  #then generate another position
  #For example
  #[['1','1','B','E','E','R','1','1','1'],
  # ['1','1','1','1','1','1','1','1','1']]

  #The word 'BEER' spans HPOS:0 VPOS:TOTAL(VPOS - 2 to TOTAL - position number 6 in the row).
  #Please note position number of row starts at 1.
  
  while not all(item == '1' for item in gridletters[hpos][vpos:total]):
   hpos = random.randint(0,len(gridletters)-1)
   vpos = random.randint(0,len(gridletters[x])-len(wordlist[x]))
   total = vpos + (len(wordlist[x]))
   
   
  for y in range(0,len(wordlist[x])):
   #Places each letter in the positions generated
   #The y variable represents each character in the current word
   #The y variable for vpos increaed by 1 each time the loop goes round
   gridletters[hpos][vpos+y] = wordlist[x][y]
 return(gridletters)

def place_word_vertically(wordlist,gridletters):

 

 for x in range(0,len(wordlist)):
     
  #Generates horizontal position. Start position is 0 and max position is length of gridletters grid minus length of current word
  hpos = random.randint(0,len(gridletters)-len(wordlist[x]))
  
  #Generates vertical position. Start position is 0 and max position is length of gridletters in the row minus 1
  vpos = random.randint(0,len(gridletters[x])-1)
  
  #While there are not all 1's (blanks) from first horizontal and vertical position generated to last horizontal and position (for length of the word)
  #then generate another postion. Each time the loop goes round one is added to horizonal position

  while not all(item == '1' for x in range(0,len(wordlist[x])) for item in gridletters[hpos+x][vpos]):
   hpos = random.randint(0,len(gridletters)-len(wordlist[x]))
   vpos = random.randint(0,len(gridletters[x])-1)
  #Places each letter in the positions generated
  #The y variable represents each character in the current word
  #The y variable for hpos increaed by 1 each time the loop goes round
  for y in range(0,len(wordlist[x])):
   gridletters[hpos+y][vpos] = wordlist[x][y]
   
 return(gridletters)

def place_word_diagonally(wordlist,gridletters):

 for x in range(0,len(wordlist)):

  #Generates horizontal position. Start position is 0 and max position is length of gridletters grid minus length of current word   
  hpos = random.randint(0,len(gridletters) - len(wordlist[x]))

  #Generates vertical position. Start position is 0 and max position is length of gridletters in the row minus 1
  vpos = random.randint(0,len(gridletters[x]) - len(wordlist[x]))

  #While there are not all 1's (blanks) from first horizontal and vertical position generated to last horizontal and position (for length of the word)
  #then generate another postion. Each time the loop goes round one is added to horizonal and vertical position
  while not all(item == '1' for x in range(0,len(wordlist[x])) for item in gridletters[hpos+x][vpos+x]):
   hpos = random.randint(0,len(gridletters)-len(wordlist[x]))
   vpos = random.randint(0,len(gridletters[x])- len(wordlist[x]))
   
  #Places each letter in the positions generated
  #The y variable represents each character in the current word
  #The y variable for hpos and vpos increaed by 1 each time the loop goes round
  for y in range(0,len(wordlist[x])):
   gridletters[hpos+y][vpos+y] = wordlist[x][y]

 return(gridletters)
    
 

def gameplay():
 welcome()
 direction = select_direction()
 wordlist = generate_wordlist()
 gridletters = initialise_grid()
 if direction == "H":
  place_word_horizontally(wordlist, gridletters)
 elif direction == "V":
  place_word_vertically(wordlist, gridletters)
 else:
  place_word_diagonally(wordlist,gridletters)
 generate_grid(gridletters)
 print_gridletters(gridletters)
 print_wordlist(gridletters, wordlist)


gameplay()
     
 








 
