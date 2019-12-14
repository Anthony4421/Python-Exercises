#Noughts and Crosses Game

import random

def introduction():
 print("""
 The object of the game is to get 3 of a kind
 in any row, column or diagonal in the 3 x 3
 grid, which is referenced like this:
 
           0 | 1 | 2 
	   ---------
	   3 | 4 | 5
	   ---------
	   6 | 7 | 8
 """)
 print("\nYou will be playing against the computer")
 print("\nLet the battle commence!")

def horizontal_wins(pos,win,winner):
 for x in range(0,8):
  if x%3 == 0 and pos[x] == "X" and pos[x+1] == "X" and pos[x+2] == "X":
   win = True
   winner = "X"
   break
  if x%3 == 0 and pos[x] == "O" and pos[x+1] == "O" and pos[x+2] == "O":
   win = True
   winner = "O"
   break
 return(win,winner)



def vertical_wins(pos,win,winner):
 for x in range(0,8):
  if x < 3 and pos[x] == "X" and pos[x+3] == "X" and pos[x+6] == "X":
   win = True
   winner = "X"
   break
  if x < 3 and pos[x] == "O" and pos[x+3] == "O" and pos[x+6] == "O":
   win = True
   winner = "O"
   break
 return(win,winner)

def diagonal_left_wins(pos,win,winner):
 if pos[2] == "X" and pos[4] == "X" and pos[6] == "X":
  print("X has won!")
  win = True
  winner = "X"
 if pos[2] == "O" and pos[4] == "O" and pos[6] == "O":
  print("O has won!")
  win = True
  winner = "O"
 return(win,winner)

def diagonal_right_wins(pos,win,winner):
 if pos[0] == "X" and pos[4] == "X" and pos[8] == "X":
  win = True
  winner = "X"
 if pos[0] == "O" and pos[4] == "O" and pos[8] == "O":
  print("O has won!")
  win = True
  winner = "O"
 return(win,winner)

def display_winner(winner,user_move,computer_move,win):
 if win == True:
  print("\n",winner,"! has won")
 if user_move == winner:
  print("\nYou must have cheated!")
 elif computer_move == winner:
  print("\nI am the greatest!")
 else:
  print("\nIt's a draw!")
  print("\nYou were lucky!")
  
 


def positions():

 pos = [" "," "," "," "," "," "," "," "," "]
 return(pos)


def board(pos):
 print("\n")
 print("\t",pos[0], "|" ,pos[1],  "|",pos[2])
 print("\t-----------")
 print("\t",pos[3], "|" ,pos[4],  "|",pos[5])
 print("\t-----------")
 print("\t",pos[6], "|" ,pos[7],  "|",pos[8])

 


def get_move(player_turn,pos,computer_move,user_move,difficulty):
    
 if player_turn == 1:
  square = int(input("\nWhich square? (0-8):"))
 else:
  if difficulty == "E":
   square = random.randint(0,8)
  else: # execute code for the hard mode
   if pos[4] == " ":
    square = 4
   elif pos[4] == user_move and pos[0] == " " and pos[1] == " " and pos[2] == " " and pos[3] == " " and pos[5] == " " and pos[6] == " " and pos[7] == " " and pos[8] == " ":
    square = 0
   elif pos[0] == computer_move and pos[1] == computer_move and pos[2] == " ":
    square = 2
   elif pos[1] == computer_move and pos[2] == computer_move and pos[0] == " ":
    square = 0
   elif pos[3] == computer_move and pos[4] == computer_move and pos[5] == " ":
    square = 5
   elif pos[4] == computer_move and pos[5] == computer_move and pos[3] == " ":
    square = 3
   elif pos[6] == computer_move and pos[7] == computer_move and pos[8] == " ":
    square = 8
   elif pos[7] == computer_move and pos[8] == computer_move and pos[6] == " ":
    square = 6
   elif pos[0] == computer_move and pos[3] == computer_move and pos[6] == " ":
    square = 6
   elif pos[4] == computer_move and pos[7] == computer_move and pos[1] == " ":
    square = 1
   elif pos[3] == computer_move and pos[6] == computer_move and pos[0] == " ":
    square = 0
   elif pos[1] == computer_move and pos[4] == computer_move and pos[7] == " ":
    square = 7
   elif pos[2] == computer_move and pos[5] == computer_move and pos[8] == " ":
    square = 8
   elif pos[5] == computer_move and pos[8] == computer_move and pos[2] == " ":
    square = 2
   elif pos[0] == computer_move and pos[4] == computer_move and pos[8] == " ":
    square = 8
   elif pos[4] == computer_move and pos[8] == computer_move and pos[0] == " ":
    square = 0
   elif pos[2] == computer_move and pos[4] == computer_move and pos[6] == " ":
    square = 6
   elif pos[4] == computer_move and pos[6] == computer_move and pos[2] == " ":
    square = 2
   elif pos[0] == computer_move and pos[2] == computer_move and pos[1] == " ":
    square = 1
   elif pos[3] == computer_move and pos[5] == computer_move and pos[4] == " ":
    square = 4
   elif pos[6] == computer_move and pos[8] == computer_move and pos[7] == " ":
    square = 7
   elif pos[0] == computer_move and pos[6] == computer_move and pos[3] == " ":
    square = 3
   elif pos[1] == computer_move and pos[7] == computer_move and pos[4] == " ":
    square = 4
   elif pos[2] == computer_move and pos[8] == computer_move and pos[5] == " ":
    square = 5
   elif pos[2] == computer_move and pos[6] == computer_move and pos[4] == " ":
    square = 4
   elif pos[0] == computer_move and pos[8] == computer_move and pos[4] == " ":
    square = 4
  #Block Wins
   elif pos[0] == user_move and pos[1] == user_move and pos[2] == " ":
    square = 2
   elif pos[1] == user_move and pos[2] == user_move and pos[0] == " ":
    square = 0
   elif pos[3] == user_move and pos[4] == user_move and pos[5] == " ":
    square = 5
   elif pos[4] == user_move and pos[5] == user_move and pos[3] == " ":
    square = 3
   elif pos[6] == user_move and pos[7] == user_move and pos[8] == " ":
    square = 8
   elif pos[7] == user_move and pos[8] == user_move and pos[6] == " ":
    square = 6
   elif pos[0] == user_move and pos[3] == user_move and pos[6] == " ":
    square = 6
   elif pos[4] == user_move and pos[7] == user_move and pos[1] == " ":
    square = 1
   elif pos[3] == user_move and pos[6] == user_move and pos[0] == " ":
    square = 0
   elif pos[1] == user_move and pos[4] == user_move and pos[7] == " ":
    square = 7
   elif pos[2] == user_move and pos[5] == user_move and pos[8] == " ":
    square = 8
   elif pos[5] == user_move and pos[8] == user_move and pos[2] == " ":
    square = 2
   elif pos[0] == user_move and pos[4] == user_move and pos[8] == " ":
    square = 8
   elif pos[4] == user_move and pos[8] == user_move and pos[0] == " ":
    square = 0
   elif pos[2] == user_move and pos[4] == user_move and pos[6] == " ":
    square = 6
   elif pos[4] == user_move and pos[6] == user_move and pos[2] == " ":
    square = 2
   elif pos[0] == user_move and pos[2] == user_move and pos[1] == " ":
    square = 1
   elif pos[3] == user_move and pos[5] == user_move and pos[4] == " ":
    square = 4
   elif pos[6] == user_move and pos[8] == user_move and pos[7] == " ":
    square = 7
   elif pos[0] == user_move and pos[6] == user_move and pos[3] == " ":
    square = 3
   elif pos[1] == user_move and pos[7] == user_move and pos[4] == " ":
    square = 4
   elif pos[2] == user_move and pos[8] == user_move and pos[5] == " ":
    square = 5
   elif pos[2] == user_move and pos[6] == user_move and pos[4] == " ":
    square = 4
   elif pos[0] == user_move and pos[8] == user_move and pos[4] == " ":
    square = 4
   else:
    square = random.randint(0,8)


   
 return(square)

def place_move(pos,square,player_turn,user_move,computer_move):
 
 if player_turn == 2:
  print("\nI will take square number", square)
  pos[square] = computer_move
 else:
  pos[square] = user_move

def check_move_valid(square,player_turn,pos):
 if pos[square] == "X" or pos[square] == "O":
  if player_turn == 1:
   print("Position already taken. Please place a valid move")
  valid_move = False
 else:
  valid_move = True
 return(valid_move)

def switch_player(player_turn):
 if player_turn == 1:
  player_turn = 2
 else:
  player_turn = 1
 return(player_turn)

def player_turns():
 player_turn = random.randint(1,2)

 if player_turn == 1:
  user_move = "X"
  print("\nUser goes first")
 else:
  user_move = "O"
 if player_turn == 2:
  computer_move = "X"
  print("\nComputer goes first")
 else:
  computer_move = "O"
 return(player_turn,user_move,computer_move)

def select_difficulty():
 difficulty = input("\nSet the difficulty level (E = Easy, H = Hard):")
 while difficulty != "E" and difficulty != "H":
  difficulty = input("\nSet the difficulty level (E = Easy, H = Hard):")
 return(difficulty)
def main():
 win = False
 winner = None
 introduction()
 difficulty = select_difficulty()
 pos = positions()
 board(pos)
 player_turn,user_move,computer_move = player_turns()
 while " " in pos and win == False:
  square = get_move(player_turn,pos,computer_move,user_move,difficulty)
  valid_move = check_move_valid(square,player_turn,pos)
  while valid_move == False:
   square = get_move(player_turn,pos,computer_move,user_move,difficulty)
   valid_move = check_move_valid(square,player_turn,pos)
  place_move(pos,square,player_turn,user_move,computer_move)
  win, winner = horizontal_wins(pos,win,winner)
  win, winner = vertical_wins(pos,win,winner)
  win, winner = diagonal_left_wins(pos,win,winner)
  win, winner = diagonal_right_wins(pos,win,winner)
  player_turn = switch_player(player_turn)
  board(pos)
  
 display_winner(winner,user_move,computer_move,win)


 
 
main()
