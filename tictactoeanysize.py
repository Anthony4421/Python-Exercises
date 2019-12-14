#Tic Tac Toe - Any Size
#Anthony Swift
#18/05/2019

'''
A two player game of tic tac toe that works on any size board specified by the user
'''

#Welcomes the player to the game
 
def welcome():
 print("\nWelcome to the Tic Tac Toe Game")
 
#Asks both players for their name

def get_player_names():
 player1 = input("\nPlayer 1 please enter your name: ")
 player2 = input("Player 2 please enter your name: ")
 
 return(player1, player2)
 
#Ask player for the board size

def get_board_size():

 size = int(input("\nPlease enter board size: "))

 return size


#Stores the game board with the moves

def game_board(size):

 board = [['1']]
 board = [(x*size) for x in board for y in range(size)]
		 
 return board
 

#Keeps track of the player scores

def player_scores():

 scores = {"p1_score" : 0, "p2_score" : 0}
 
 return(scores)
 
#Displays the scores to the players
 
def display_scores(player1, player2, scores):

 print("\nSo far",player1,"has won",scores['p1_score'],"games and",player2,"has won",scores['p2_score'],"games")

 
#Prints the game board

def print_board(board):
 print("\n")
 for x in range(0,len(board)):
  print(board[x])

#Works out which players turn it is
#By default player 1 (X) goes first
#Each time player has made their move
#Player turn switches to the other player


def player_turns(turn, player1, player2):
 if turn == 1:
  turn = 2
  player = player1
 elif turn == 2:
  turn = 1
  player = player2
  
 return(turn, player)
  
#Asks player for their move in the format (row,col)
#splits the string entered by the user
#Ensures start position starts at 1

def ask_player_for_move(player):

 print("\n")
 print(player,"it is your turn")
 move = input("Please enter your move (in the format row,col): ")
 move = move.split(",")
 row = int(move[0])-1
 col = int(move[1])-1

 return(row,col)

#Checks the move entered by player has not already been taken
#Displays to the user if the move has already been taken

def check_move_valid(board,row,col,move_valid):

 if board[row][col] == "X" or board[row][col] == "O":
  print("\nYou cannot make a move here. Please re-enter")
  move_valid = False
 else:
  move_valid = True
 return move_valid
  
#Places the move entered by the player on the game board
#Enters x on the board if it is player1's turn
#Enters O on the board if it is player2's turn

def place_move(row, col, board, player, player1, player2):
 if player == player1:
  board[row][col] = "X"
 else:
  board[row][col] = "O"
  
 return board
 
#Checks for horizontal wins
	 
def horizontal_wins(board, player1, player2, winner, win):
 total = 0
 for x in range(0,len(board)):
  for y in range(0,len(board)):
   if y == 0:
    total = 0
   if board[x][y] == "X":
    total +=1
   if total == len(board):
    winner = player1
    win = True
	
 for x in range(0,len(board)):
  for y in range(0,len(board)):
   if y == 0:
    total = 0
   if board[x][y] == "O":
    total +=1
   if total == len(board):
    winner = player2
    win = True
   
 
 return(winner, win)
 
 
#Check for vertical wins

def vertical_wins(board, player1, player2, winner, win):

 total = 0
 for y in range(0,len(board)):
  for x in range(0,len(board)):
   if x == 0:
    total = 0
   if board[x][y] == "X":
    total +=1
   if total == len(board):
    winner = player1
    win = True
	
 for y in range(0,len(board)):
  for x in range(0,len(board)):
   if x == 0:
    total = 0
   if board[x][y] == "O":
    total +=1
   if total == len(board):
    winner = player2
    win = True
 

   
 return(winner, win)
 
#Check for diagonal left wins

def diagonal_left_wins(board, player1, player2, winner, win):
 
 total = 0
 for x in range(0,len(board)):
  for y in range(0,len(board)):
   if board[x][y] == "X" and x==y:
    total +=1
   if total == len(board):
    winner = player1
    win = True
	
 total = 0	
 for x in range(0,len(board)):
  for y in range(0,len(board)):
   if board[x][y] == "O" and x==y:
    total +=1
   if total == len(board):
    winner = player2
    win = True
 return(winner, win)
  
#Check for diagonal right wins
 
def diagonal_right_wins(board, player1, player2, winner, win):
 
 total = 0
 for x in range(0,len(board)):
  for y in range(0,len(board)):
   if board[x][y] == "X" and y == (len(board)-1) - x:
    total +=1
   if total == len(board):
    winner = player1
    win = True
	
 total = 0
 for x in range(0,len(board)):
  for y in range(0,len(board)):
   if board[x][y] == "O" and y == (len(board)-1) - x:
    total +=1
   if total == len(board):
    winner = player2
    win = True
	
 return(winner, win)
  
#Checks if the board is full during each game
#Ends the game if the board is full

def check_board_full(board,board_full):
 total = 0
 for x in range(0,len(board)):
  for y in range(0,len(board)):
   if board[x][y] != "1":
    total +=1
 if total == len(board) * len(board):
  board_full = True
 
  
 return board_full
 
#Displays the winner to the players
 
def display_winner(win, winner):
 if win == True:
  print("\nCongratulations,",winner,"! You have won")
 else:
  print("\nThe game is a draw. The game will now end")
  
#Asks player if they would like to play again

def play_again(gameplay):
 gameplay = input("\nWould you like to play again (Y/N): ")
 gameplay = gameplay.upper()
 
 return gameplay
 
#Updates the player scores at the end of each game
 
def update_player_Scores(winner, scores, player1, player2):
 if winner == player1:
  scores['p1_score'] +=1
 elif winner == player2:
  scores['p2_score'] +=1
 else:
  scores['p1_score'] +=1
  scores['p2_score'] +=1
 return scores
 
  
def main():
 gameplay = "Y"
 game_number = 0
 while gameplay == "Y":
  game_number +=1
  win = False
  move_valid = True
  board_full = False
  turn = 1
  winner = ""
  if game_number == 1:
   welcome()
   scores = player_scores()
   player1, player2 = get_player_names()
   size = get_board_size()
  board = game_board(size)
  while board_full == False and win == False:
   print_board(board)
   turn, player = player_turns(turn, player1, player2)
   row, col = ask_player_for_move(player)
   move_valid = check_move_valid(board,row,col,move_valid)
   while move_valid == False:
    print_board(board)
    row, col = ask_player_for_move(player)
    move_valid = check_move_valid(board,row,col,move_valid)
   board = place_move(row, col, board, player, player1, player2)
   board_full = check_board_full(board,board_full)
   winner, win = horizontal_wins(board, player1, player2, winner, win)
   winner, win = vertical_wins(board, player1, player2, winner, win)
   winner, win = diagonal_left_wins(board, player1, player2, winner, win)
   winner, win = diagonal_right_wins(board, player1, player2, winner, win)
  print_board(board)
  display_winner(win, winner)
  update_player_Scores(winner, scores, player1, player2)
  display_scores(player1, player2, scores)
  gameplay = play_again(gameplay)
 
main()
 
  


 