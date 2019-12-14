#Bingo Game
#Anthony Swift
#06/05/2019

'''

A simple bingo game. Player is presented with a randomly generated grid of numbers.
Player is asked to enter the number called out by the caller, each time a number is called out.
A chip ('X') is placed on the grid when the number entered (that has been called) matches a number on the grid.
Player wins if they match 5 numbers in a row on the grid (diagonally, vertically or horizontally).

The bingo grid is generated in line with standard bingo rules:
 In the first column (B) - Random numbers are generated between 1 and 15.
 In the second column (I) - Random numbers are generated between 16 and 30.
 In the third column (N) - Random numbers are generated between 31 and 45 (with a free chip in the middle).
 In the fourth column (G) - Random numbers are generated between 46 and 60.
 In the fifth column (o) - Random numbers are generated between 61 and 75.
 
'''


import random

#Welcome player to the game

def welcome():
 print("\nWelcome to the Bingo Game.")

#Initialise the bingo grid

def initialise_grid():

 grid = [['','','','','' ],
         ['','','','','' ],
         ['','','','','' ],
         ['','','','','' ],
         ['','','','','' ]]
 return grid

#Randomly generates numbers in the first column (B) of the bingo grid
#Ensures the numbers are between 1 and 15

def generate_b_column(grid):
 
 b_nums = []
 
 for x in range(0,5):
  num = random.randint(1,15)
  while num in b_nums:
   num = random.randint(1,15)
  b_nums.append(num)
  
 for x in range(0,5):
  grid[x][0] = b_nums[x]
  
 return grid

#Randomly generates numbers in the second column (I) of the bingo grid
#Ensures the numbers are between 16 and 30

def generate_i_column(grid):
 i_nums = []
 
 for x in range(0,5):
  num = random.randint(16,30)
  while num in i_nums:
   num = random.randint(16,30)
  i_nums.append(num)
  
 for x in range(0,5):
  grid[x][1] = i_nums[x]
  
 return grid

#Randomly generates numbers in the third column (N) of the bingo grid
#Ensures the numbers are between 31 and 45
#Places a chip in the middle position of the grid as this is a free move.

def generate_n_column(grid):
 n_nums = []
 
 for x in range(0,5):
  if x == 2:
   n_nums.append("X")
  else:
   num = random.randint(31,45)
   while num in n_nums:
    num = random.randint(31,45)
   n_nums.append(num)
  
 for x in range(0,5):
  grid[x][2] = n_nums[x]
 return grid
 
#Randomly generates numbers in the fourth column (G) of the bingo grid
#Ensures the numbers are between 46 and 60

def generate_g_column(grid):
 g_nums = []
 
 for x in range(0,5):
  num = random.randint(46,60)
  while num in g_nums:
   num = random.randint(46,60)
  g_nums.append(num)
  
 for x in range(0,5):
  grid[x][3] = g_nums[x]
 return grid

#Randomly generates numbers in the fifth column (O) of the bingo grid
#Ensures the numbers are between 61 and 75

def generate_o_column(grid):
 o_nums = []
 
 for x in range(0,5):
  num = random.randint(61,75)
  while num in o_nums:
   num = random.randint(61,75)
  o_nums.append(num)
  
 for x in range(0,5):
  grid[x][4] = o_nums[x]
 return grid

#Asks player to enter number called by the caller

def enter_number_called():
 print("\n")
 num_called = int(input("Please enter the number called: "))
 return num_called
 
#If the number entered by player matches a number on the grid
#A chip (X) is placed on the grid where the number matches

def place_chips(num_called,grid):
 for x in range(0,5):
  for y in range(0,5):
   if grid[x][y] == num_called:
    grid[x][y] = 'X'
 return grid
 
#Checks to see if the player has 5 chips (X's) in a row horizontally on the grid
#Lets the player know if they have won.

def check_horizontal_win(grid, win):
 for x in range(0,5):
  if grid[x][0] == 'X' and grid[x][1] == 'X' and grid[x][2] == 'X' and grid[x][3] == 'X' and grid[x][4] == 'X':
   print("You have won! BINGO!! ")
   win = True
 return win

#Checks to see if the player has 5 chips (X's) in a row vertically on the grid
#Lets the player know if they have won.

def check_vertical_win(grid, win):
 for y in range(0,5):
  if grid[0][y] == 'X' and grid[1][y] == 'X' and grid[2][y] == 'X' and grid[3][y] == 'X' and grid[4][y] == 'X':
   print("You have won! BINGO!! ")
   win = True
 return win

#Checks to see if the player has 5 chips (X's) in a row diagonally left on the grid
#Lets the player know if they have won.

def check_diagonal_left_win(grid, win):
 if grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X' and grid[3][3] == 'X' and grid[4][4] == 'X':
  print("You have won! BINGO!! ")
  win = True
 return win
 
#Checks to see if the player has 5 chips (X's) in a row diagonally right on the grid
#Lets the player know if they have won.

def check_diagonal_right_win(grid, win):
 if grid[0][4] == 'X' and grid[1][3] == 'X' and grid[2][2] == 'X' and grid[3][1] == 'X' and grid[4][0] == 'X':
  print("You have won! BINGO!! ")
  win = True
 return win
 
#Prints the grid

def print_grid(grid):
 print("\n")
 print("Bingo Board:")
 print("\n")
 for x in range(0,5):
  print(grid[x])

#The main function
 
def main():
 win = False
 welcome()
 grid = initialise_grid()
 grid = generate_b_column(grid)
 grid = generate_i_column(grid)
 grid = generate_n_column(grid)
 grid = generate_g_column(grid)
 grid = generate_o_column(grid)
 print_grid(grid)
 while win == False:
  num_called = enter_number_called()
  grid = place_chips(num_called,grid)
  win = check_horizontal_win(grid, win)
  win = check_vertical_win(grid, win)
  win = check_diagonal_left_win(grid, win)
  win = check_diagonal_right_win(grid, win)
  print_grid(grid)
  
 
main()

 
  