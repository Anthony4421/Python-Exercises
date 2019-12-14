#Connect Four Game
#Anthony Swift
#21/08/2017

#Keep track of scores

def scores():

 player_scores = {'p1score': 0, 'p2score': 0}

 return(player_scores)

#Welcome player to the game

def welcome():
 print("\nWelcome to the Connect Four Game")
 print("\n")
 
#Ask players for names

def get_players():
 player1 = input("Player1 please enter your name: ")
 player2 = input("player2 please enter your name: ")
 print("\n")

 return(player1, player2)

#Welcome the players

def welcome_players(player1, player2):
 print("Welcome to the game" ,player1, "and" ,player2)
 print("\n")

#Setup the game board 

def board_setup():
 board = [['1','1','1','1','1','1','1'],
          ['1','1','1','1','1','1','1'],
          ['1','1','1','1','1','1','1'],
          ['1','1','1','1','1','1','1'],
          ['1','1','1','1','1','1','1'],
          ['1','1','1','1','1','1','1']]

 length = len(board)

 return(board, length)

#Print the game board

def print_board(board, length):
 for x in range(0,length):
  print(board[x])

#Ask player 1 for move
#If the move is not between 0 and 6 ask player to re-enter

def get_player1_move(player1):
 print("\n")
 print(player1, "(red) it is your turn")
 move = int(input("Please enter the column number you would like to place your move: "))
 while (move < 0) or (move > 6):
  move = int(input("Please enter the column number you would like to place your move: "))
 print("\n")
 #print(move)
 return(move)

#Ask player 2 for move
#If the move is not between 0 and 6 ask player to re-enter

def get_player2_move(player2):
 print("\n")
 print(player2, "(yellow) it is your turn")
 move = int(input("Please enter the column number you would like to place your move: "))
 while (move < 0) or (move > 6):
  move = int(input("Please enter the column number you would like to place your move: "))
 print("\n")
 #print(move)
 return(move)

#Check for horizontal wins

def check_hwins(board, length, player1, player2, wins, winner):

 for x in range(0,length):
  for y in range(0,4): #only loops to 4th position to check if four in a row
   if (board[x][y] == "R") and (board[x][y+1] == "R") and (board[x][y+2] == "R") and (board[x][y+3] == "R"):
     wins = True
     winner = player1
   if (board[x][y] == "Y") and (board[x][y+1] == "Y") and (board[x][y+2] == "Y") and (board[x][y+3] == "Y"):
     wins = True
     winner = player2
 return(wins, winner)

#Check for vertical wins

def check_vwins(board, length, player1, player2, wins, winner):

 for x in range(0,3):
  for y in range(0,7):
   if (board[x][y] == "R") and (board[x+1][y] == "R") and (board[x+2][y] == "R") and (board[x+3][y] == "R"):
    wins = True
    winner = player1
   if (board[x][y] == "Y") and (board[x+1][y] == "Y") and (board[x+2][y] == "Y") and (board[x+3][y] == "Y"):
    wins = True
    winner = player2
 return(wins, winner)

#Check for diagonal left wins

def check_dleftwins(board, length, player1, player2, wins, winner):

 for x in range(0,3):
  for y in range(0,7): 
   if (board[x][y] == "R") and (board[x+1][y-1] == "R") and (board[x+2][y-2] == "R") and (board[x+3][y-3] == "R"):
    wins = True
    winner = player1
   if (board[x][y] == "Y") and (board[x+1][y-1] == "Y") and (board[x+2][y-2] == "Y") and (board[x+3][y-3] == "Y"):
    wins = True
    winner = player2
 return(wins, winner)
 
#Check for diagonal right wins

def check_drightwins(board, length, player1, player2, wins, winner):

 for x in range(0,3):
  for y in range(0,4): #Had to be really careful how I specified the for loop here
   if (board[x][y] == "R") and (board[x+1][y+1] == "R") and (board[x+2][y+2] == "R") and (board[x+3][y+3] == "R"):
    wins = True
    winner = player1
   if (board[x][y] == "Y") and (board[x+1][y+1] == "Y") and (board[x+2][y+2] == "Y") and (board[x+3][y+3] == "Y"):
    wins = True
    winner = player2
 return(wins, winner)

#Checks if a column is full when a move is made
#Does not allow player to make a move if column is full

def check_col_free(move, board, length):
 moves_made = 0
 moves_valid = False
 for x in range(0,length):
  if (board[x][move] == "R") or (board[x][move] == "Y") :
   moves_made = moves_made + 1

 if moves_made == 6:
  print("The column is full. You cannot make a move here")
 else:
  moves_valid = True
 print("\n")

 return(moves_made,moves_valid)
 
#Places move made by player 1 in position

def place_move1(board, move, length):
 for x in range(0,length):
  if board[(length-1) - x][move] == "1":
   board[(length-1) - x][move] = "R"
   break

#Places move made by player 2 in position

def place_move2(board, move, length):
 for x in range(0,length):
  if board[(length-1) - x][move] == "1":
   board[(length-1) - x][move] = "Y"
   break

#Display the winner

def display_winner(winner):
 print("\nYou have won", winner)

#Ask players if they would like to play again
#Convert response to uppercase
#If player does not enter 'Y' or 'N' ask player to re-enter response

def get_response():
 response = input("\nWould you like to play again? (Y/N)")
 response = response.upper()
 while response != "Y" and response != "N":
  response = input("\nWould you like to play again? (Y/N)")
  response = response.upper()
 

 return(response)

#Update the player scores

def update_player_scores(winner, player_scores, player1, player2):

 if winner == player1:
  p1_score = player_scores['p1score']
  p1_score = p1_score + 1
  player_scores['p1score'] = p1_score
 if winner == player2:
  p2_score = player_scores['p2score']
  p2_score = p2_score + 1
  player_scores['p2score'] = p2_score

#Display player scores at the end of the game

def display_score(player1, player2, player_scores):

 print("So far", player1, "has won", player_scores['p1score'], "games and", player2, "has won" ,player_scores['p2score'])
 
#The main function

def gameplay():
 player_scores = scores()
 response = "Y"
 game_number = 0
 while response == "Y":
  game_number = game_number + 1
  moves_valid = False
  moves_made = 0
  wins = False
  winner = ""
  welcome()
  if game_number == 1:
   player1, player2 = get_players()
   welcome_players(player1, player2)
   board, length = board_setup()
   print_board(board, length)
  else:
   welcome_players(player1, player2)
   board, length = board_setup()
   print_board(board, length)
  while wins == False:
   if wins == True:
    break
   else:
    while moves_valid == False:
     move = get_player1_move(player1)
     moves_made, moves_valid = check_col_free(move, board, length)
    else:
     place_move1(board, move, length)
     wins, winner = check_hwins(board, length, player1, player2, wins, winner)
     wins, winner = check_vwins(board, length, player1, player2, wins, winner)
     wins, winner = check_dleftwins(board, length, player1, player2, wins, winner)
     wins, winner = check_drightwins(board, length, player1, player2, wins, winner)
     print_board(board, length)
     moves_valid = False
   if wins == True:
    break
   else:
    while moves_valid == False:
     move = get_player2_move(player2)
     moves_made, moves_valid = check_col_free(move, board, length)
    else:
     place_move2(board, move, length)
     wins, winner = check_hwins(board, length, player1, player2, wins, winner)
     wins, winner = check_vwins(board, length, player1, player2, wins, winner)
     wins, winner = check_dleftwins(board, length, player1, player2, wins, winner)
     wins, winner = check_drightwins(board, length, player1, player2, wins, winner)
     print_board(board, length)
     moves_valid = False
  update_player_scores(winner, player_scores, player1, player2)
  display_winner(winner)
  display_score(player1, player2, player_scores)
  response = get_response()
  

 
 



 
 
 
 

gameplay()
