#Strike it Lucky Game
#Anthony Swift

import random

'''
User is presented with 10 columns of screens with 3 screens in each column.
In each screen in each column, behind each screen is either a safe move, a hot spot or a question.
The user cannot see the moves behind the screens until they start to play the game.
At the start of the game, the moves are shuffled so there is one of each type of move in each column.
The player moves through each screen/column individually and is asked to pick top, middle or bottom.
The move for that particular screen is then revealed.
If the screen displays a safe move '>>' then the player can move to the next column.
If the screen displays an Hot Spot 'H' then the player loses a life before moving to the next column.
If the screen displays a question 'Q' the player is asked a true or false question.
If the player gets the question correct the screen becomes a safe move and they move on.
If the player gets the question wrong the screen becomes a hot spot and they lose a life before moving on.
When the player has run out of lives/Hot Spots its game over:
When the player reaches the end they have won.
 The number of hot spots a player is allowed is determind by how much money they decide to play for:
  £2000 - Allowed 4 Hot Spots.
  £3000 - Allowed 3 Hot Spots.
  £4000 - Allowed 2 Hot Spots.
'''

#Welcome player to the game.
def welcome():
 print("\nWelcome to the Strike it Lucky Game")

#Give the player option to display rules.
def display_rules():
 rules_option = input("\nWould you like to display the rules(Y/N)? ")
 rules_option = rules_option.upper()
 return(rules_option)

#Check player has entered a valid option
#When asked to display rules.
def check_rules_option(rules_option):
 rules_option_valid = True
 if rules_option !="Y" and rules_option != "N":
  print("\nThe option was not valid. Please enter again")
  rules_option_valid = False
 return(rules_option_valid)

#Displays the rules.
def rules():
 print("""
 
Rules:

The player is presented with 10 columns of screens
with 3 screens in each column. 
In each screen in each column, behind each screen is either
a safe move, a hot spot or a question. 
The user cannot see the moves behind the screens
until they start to play the game. 

At the start of the game, the moves are shuffled 
so there is one of each type of move in each column.
The player moves through each screen/column individually 
and is asked to pick top, middle or bottom.
The move for that particular screen is then revealed.

If the screen displays a safe move '>>' 
then the player can move to the next column.
If the screen displays an Hot Spot 'H' 
then the player loses a life before moving to the next column.
If the screen displays a question 'Q' 
the player is asked a true or false question.
If the player gets the question correct 
the screen becomes a safe move and they move on.
If the player gets the question wrong 
the screen becomes a hot spot and they lose a life before moving on.

When the player has run out of lives/Hot Spots its game over.
When the player reaches the end they have won.

The number of hot spots a player is allowed is 
determind by how much money they decide to play for:
  £2000 - Allowed 4 Hot Spots.
  £3000 - Allowed 3 Hot Spots.
  £4000 - Allowed 2 Hot Spots.     
""")

#Ask the player how much money they would like to play for.
def ask_for_amount_playing_for():

 amount = input("\nHow much would you like to play for? \nPlease enter either 2000, 3000 or 4000: ")
 print("\n")
 
 return(amount)

#Check the amount the player has entered to play for is valid.
def check_amount_asked_for(amount):
 amount_valid = True
 if amount != "2000" and amount != "3000" and amount != "4000" or amount.isnumeric() == False:
  amount_valid = False
  print("\nThe amount is not valid")
  print("\nPlease enter the amount you would like to play again")
  
 return(amount_valid)  

#Set the number of hotspots 
#Based on the amount player has decided to play for.
def set_hotspots(amount):
 if amount == "2000":
  number_of_hotspots = 4
 elif amount == "3000":
  number_of_hotspots = 3
 else:
  number_of_hotspots = 2

 return(number_of_hotspots)
 

#Sets up the screen to random generate all the moves.
#Set user screen to place the moves throughout the game.
def screen_setup():

 
 screens = [['','','','','','','','','',''],
            ['','','','','','','','','',''],
		    [' ','','','','','','','','','']]
			
 user_screens = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                 [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
		         [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
		   
 return(screens,user_screens)

#Randomly generates the moves into the main screen.
#In each column places a safe move (>) hot spot (H) and a question (Q).
def generate_moves(screens):
 for y in range(0,10):
  for x in range(0,3):
   if x == 0:
    moves = ['Q','H','>']
   rand = random.choice(moves)
   screens[x][y] = rand
   moves.remove(rand)

#Prints the main screen where all the moves have been generated.
#This was done as a test only to check one of each move was generated 
#in each column before the game.
def print_screens(screens):

 for x in range(0,len(screens)):
  print(str(screens[x]).replace("'",""))

#Display the amount the user is playing for.  
def display_amount_playing_for(amount):
 print("\nYou are playing for £",amount)

#Prints the user screens.
#Each time the player has made a move
#prints the results of each move in each column.
def print_user_screens(user_screens):
 print("\n")
 for x in range(0,len(user_screens)):
  print(str(user_screens[x]).replace("'",""))

#Asks the player for move in each column.  
def ask_player_for_move():

 move = input("\nPlease enter your move: Top(T), Middle(M) or Bottom(B)? ")
 move = move.upper()
 
 return(move)

#Checks the move is valid.
def check_player_move_valid(move):
 move_valid = True
 if move != "T" and move != "M" and move != "B" or move.isnumeric() == True:
  move_valid = False
  print("\nThe move is not valid")
  print("\nPlease enter move you would like to play again")
  
 return(move_valid)  
 


#Displays the move on the board.
#Behind the screen the player has picked.
def place_move(move,screens,user_screens,screen_number):
 for y in range(0,10):
  for x in range(0,3):
   if move == "T" and y == screen_number:
    user_screens[0][y] = screens[0][y]
   if move == "M" and y == screen_number:
    user_screens[1][y] = screens[1][y]
   if move == "B" and y == screen_number:
    user_screens[2][y] = screens[2][y]
 return(move)
 
#Displays the move displayed based on what the player has picked.
def display_move_details(move,screen_number,user_screens,number_of_hotspots):
 question = False
 for y in range(0,10):
  for x in range(0,3):
   if y == screen_number:
    if user_screens[0][y] == ">" or user_screens[1][y] == ">" or user_screens[2][y] == ">":
     print("\nSafe Move")
     break
    if user_screens[0][y] == "H" or user_screens[1][y] == "H" or user_screens[2][y] == "H":
     number_of_hotspots -=1
     print("\nHot Spot. You have", number_of_hotspots, "hotspots remaining")
     break
    if user_screens[0][y] == "Q" or user_screens[1][y] == "Q" or user_screens[2][y] == "Q":
     print("\nQuestion:")
     question = True
     break 
 
 return(number_of_hotspots,question)

#If the players move reveals a question.
#Randomly generates question from file
#and prints to the screen.
def display_question(question_number, asked):
 flag = ""
 
 print("\n")
 print(asked)
 with open('questions.txt', 'r') as file:
  line_number = 1
  for line in file:
   if line_number == question_number:
    flag = line[0]
    print(line[2:])
   line_number +=1
 return(flag)
 

#Generates question number
#Checks questions asked to ensure the same question is not asked more than once

def generate_question_number(asked):
 question_number = random.randint(1,10)
 while question_number in asked:
  question_number = random.randint(1,10)
 asked.append(question_number)
 return(question_number)

#Keeps track of questions asked
def questions_asked():
 asked = []
 return(asked)

 
 
 
#If the player has reached the last screen within the number of allowed hotspots
#displays the player has won
#If the player has reached the max number of hotspots displays game over.	
def display_win_or_loss(screen_number,number_of_hotspots):
 if screen_number == 10 and number_of_hotspots > 0:
  print("Congratulations, you have won")
 else:
  print("You have run out of Hot Spots. It is game over for you!")

#Ask for players answer to question if one has been generated.  
def get_answer_to_question():
 answer = input("Is that True (T) or False (F)?")
 answer = answer.upper()
 return(answer)

#Check player has entered a valid option to question.
def check_answer_valid(answer):
 answer_valid = True
 if answer != "T" and answer != "F" or answer.isnumeric() == True:
  answer_valid = False
  print("\nThe answer is not valid")
  print("\nPlease enter answer again")
  
 return(answer_valid)   

#Displays whether player has answered question correctly or not.
def display_result(answer,flag):
 correct_answer = False
 if answer == flag:
  print("Correct")
  correct_answer = True
 else:
  print("Incorrect")
 return(correct_answer)
 
#If player has got the question correct the current move changes to safe move
#and updates on the user screens.
#If player gets a question incorrect
#move changes to hot spot
def place_move_after_question_answered(correct_answer,screen_number,user_screens):
 for y in range(0,10):
  for x in range(0,3):
   if y == screen_number:
    if correct_answer == True:
     if user_screens[0][y] == "Q":
      user_screens[0][y] = ">"
     elif user_screens[1][y] == "Q":
      user_screens[1][y] = ">"
     elif user_screens[2][y] == "Q":
      user_screens[2][y] = ">"
    else:
     if user_screens[0][y] == "Q":
      user_screens[0][y] = "H"
     elif user_screens[1][y] == "Q":
      user_screens[1][y] = "H"
     elif user_screens[2][y] == "Q":
      user_screens[2][y] = "H"
	  
#Keeps track of the screen number/column number the player in on	  
def update_screen_number(screen_number):
 screen_number +=1
 return(screen_number)
 
def main():
 screen_number = 0
 asked = questions_asked()
 welcome()
 rules_option = display_rules()
 rules_option_valid = check_rules_option(rules_option)
 while rules_option_valid == False:
  rules_option = display_rules()
  rules_option_valid = check_rules_option(rules_option)
 if rules_option == "Y":
  rules()
 amount = ask_for_amount_playing_for()
 amount_valid = check_amount_asked_for(amount)
 while amount_valid == False:
  amount = ask_for_amount_playing_for()
  amount_valid = check_amount_asked_for(amount)
 number_of_hotspots = set_hotspots(amount)
 screens, user_screens = screen_setup()
 generate_moves(screens)
 print_screens(screens)
 display_amount_playing_for(amount)
 print_user_screens(user_screens)
 while screen_number < 10 and number_of_hotspots > 0:
  move = ask_player_for_move()
  move_valid = check_player_move_valid(move)
  while move_valid == False:
   move = ask_player_for_move()
   move_valid = check_player_move_valid(move)
  move = place_move(move,screens,user_screens,screen_number)
  print_user_screens(user_screens)
  number_of_hotspots,question = display_move_details(move,screen_number,user_screens,number_of_hotspots)
  if question == True:
   question_number = generate_question_number(asked)
   flag = display_question(question_number, asked)
   answer = get_answer_to_question()
   answer_valid = check_answer_valid(answer)
   while answer_valid == False:
    answer = get_answer_to_question()
    answer_valid = check_answer_valid(answer)
   correct_answer = display_result(answer,flag)
   place_move_after_question_answered(correct_answer,screen_number,user_screens)
   print_user_screens(user_screens)
   number_of_hotspots,question = display_move_details(move,screen_number,user_screens,number_of_hotspots)
  screen_number = update_screen_number(screen_number)
 display_win_or_loss(screen_number,number_of_hotspots) 
 


 
 
main()


  

