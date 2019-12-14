#Obstruction Game
#Anthony Swift
#21/05/18

#Welcome player to game

def welcome():
 print("\nWelcome to the Obstruction Game")

#Display the game instructions

def instructions():

 print("""
This is a two player game where you will take turns marking squares on a grid.
One player with be X's the other player will be O'S.
You will take turns selecting a move in the format (row,col).
The restriction is you can only play in a cell if all it's neighbours are empty.
The first player unable to move loses.
""")

#Ask players for names

def get_players():
 player1 = input("\nPlayer 1 please enter your name: ")
 player2 = input("Player 2 please enter your name: ")
 print("\n")
 return(player1, player2)

#Ask for board size

def get_board_size():

 size = input("Please enter board size in format (rows,cols): ")
 size = size.split(",")
 rows = int(size[0])
 cols = int(size[1])

 return(rows,cols)

#Generates the board size based on what the player specifies

def board_setup(rows,cols):

 board = [['1']]
 board = [(x*cols) for x in board for y in range(rows)]

 return(board)

#Prints the board

def print_board(board):
 for x in range(0,len(board)):
  
  print(board[x])

#Displays which player turn it is  

def display_player_turn(turn,player1,player2):
 if turn == 1:
  print(player1, "it is your turn")
 elif turn == 2:
  print(player2, "it is your turn")

#ask player for move

def get_player_move(board):

 #print("\n")
 move = input("\nPlease enter your move in the format (row,col)")
 move = move.split(",")
 row = int(move[0])
 col = int(move[1])
 print("\n")
 return(row,col)

# Works out which player turn it is

def player_turn(turn):
 if turn == 0 or turn == 2:
  turn = 1
 elif turn == 1:
  turn = 2
 print("\n") 
 return(turn)

#Checks if the move made by the player is valid

def check_move_valid(row,col,board):
 valid_move = False
 if board[row-1][col-1] == "X" or board[row-1][col-1] == "O" or board[row-1][col-1] == "-": 
  print("You cannot make a move here. Please re-enter\n")
 else:
  valid_move = True
 return(valid_move)

#Places move on the board

def place_move(row,col,board,turn):
 if turn == 1:
  board[row-1][col-1] = "X"
 else:
  board[row-1][col-1] = "O"

#Adds restrictions to the board once a move is placed by the player

def add_restrictions(board,rows,cols):
 for x in range(0,rows):
  for y in range(0,cols):
   if board[x][y] == "X" or board [x][y] == "O":
    if x == 0 and y == 0:
     board[x][y+1] = "-"
     board[x+1][y] = "-"
     board[x+1][y+1] = "-"
    elif x != 0 and x != rows-1 and y == 0:
     board[x-1][y] = "-"
     board[x-1][y+1] = "-"
     board[x][y+1] = "-"
     board[x+1][y] =  "-"
     board[x+1][y+1] = "-"
    elif x == rows-1 and y == 0:
     board[x-1][y] = "-"
     board[x-1][y+1] = "-"
     board[x][y+1] = "-"
    elif x == 0 and y != 0 and y != cols-1:
     board[x][y-1] = "-"
     board[x+1][y-1] = "-"
     board[x+1][y] = "-"
     board[x+1][y+1] = "-"
     board[x][y+1] = "-"
    elif x == 0 and y == cols-1:
     board[x][y-1] = "-"
     board[x+1][y-1] = "-"
     board[x+1][y] = "-"
    elif y == cols-1 and x != 0 and x != rows-1:
     board[x-1][y-1] = "-"
     board[x-1][y] = "-"
     board[x][y-1] = "-"
     board[x+1][y-1] = "-"
     board[x+1][y] = "-"
    elif x == rows-1 and y != 0 and y != cols-1:
     board[x][y-1] = "-"
     board[x-1][y-1] = "-"
     board[x-1][y] = "-"
     board[x-1][y+1] = "-"
     board[x][y+1] = "-"
    elif x == rows-1 and y == cols-1:
     board[x-1][y-1] = "-"
     board[x-1][y] = "-"
     board[x][y-1] = "-"
    else:
     board[x-1][y-1] = "-"
     board[x-1][y] = "-"
     board[x-1][y+1] = "-"
     board[x][y+1] = "-"
     board[x+1][y+1] = "-"
     board[x+1][y] = "-"
     board[x+1][y-1] = "-"
     board[x][y-1] = "-"

#Checks each position on the board to see if it is not blank
#Adds 1 to total if the move is not blank
#Sets the wins flag to true when all positions are taken
#and there are no blank positions remaining

def check_win(board,wins):
 total = 0
 for x in range(0,len(board)):
  if "1" not in board[x]:
   total +=1
 if total == len(board):
  wins = True
 return(wins)

#Display the winner

def display_winner(player1,player2,turn):
 print("\n")
 if turn == 1:
  print("Congratulations", player1, "you have won")
 else:
  print("Congratulations", player2, "you have won")


#The main function
 
def gameplay():
 wins = False
 
 turn = 0
 welcome()
 instructions()
 rows,cols = get_board_size()
 board = board_setup(rows,cols)
 player1, player2 = get_players()
 print_board(board)
 while wins == False:
  turn = player_turn(turn)
  display_player_turn(turn,player1,player2)
  row, col = get_player_move(board)
  valid_move = check_move_valid(row,col,board)
  while valid_move == False:
   print_board(board)
   row, col = get_player_move(board)
   valid_move = check_move_valid(row,col,board)
   if valid_move == True: 
    break
  place_move(row,col,board,turn)
  add_restrictions(board,rows,cols)
  print_board(board)
  wins = check_win(board,wins)
  if wins == True:
   break
 display_winner(player1,player2,turn)
gameplay()




