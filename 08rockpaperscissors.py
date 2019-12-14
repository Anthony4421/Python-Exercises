#Practice Python
#Exercise 8 - Rock Paper Scissors
#Anthony Swift
#14/02/2019

def welcome():
 print("\nWelcome to the Rock Paper Scissors Game.")
 
def get_player1():
 player1 = input("\nPlayer 1 please enter your name: ")
 return player1
 
def get_player2():
 player2 = input("Player 2 please enter your name: ")
 return player2
 
def player1_play(player1):
 print("\n")
 print(player1,"it is your turn.")
 p1_play = input("Please enter your move - Rock, Paper or Scissors: ")
 p1_play = p1_play.lower()
 return p1_play
 
def player2_play(player2):
 print("\n")
 print(player2,"it is your turn.")
 p2_play = input("Please enter your move - Rock, Paper or Scissors: ")
 p2_play = p2_play.lower()
 return p2_play
 
def check_valid_play_p1(p1_play, valid_play): 
 if (p1_play) != "rock" and (p1_play) != "scissors" and (p1_play) != "paper":
  print("Invalid entry. Please re-enter")
  valid_play = False
 else:
  valid_play = True
 return valid_play
 
def check_valid_play_p2(p2_play, valid_play): 
 if (p2_play) != "rock" and (p2_play) != "scissors" and (p2_play) != "paper":
  print("Invalid entry. Please re-enter")
  valid_play = False
 return valid_play
 
 
def compare_plays(p1_play, p2_play, player1, player2):
 if (p1_play) == "rock" and (p2_play) == "scissors":
  winner = player1
 elif (p1_play) == "rock" and (p2_play) == "paper":
  winner = player2
 elif (p1_play) == "scissors" and (p2_play) == "paper":
  winner = player1
 elif (p1_play) == "scissors" and (p2_play) == "rock":
  winner = player2
 elif (p1_play) == "paper" and (p2_play) == "rock":
  winner = player1
 elif (p1_play) == "paper" and (p2_play) == "scissors":
  winner = player2
 else:
  winner = "draw"

 return winner

def display_winner(winner): 

 if winner == "draw":
  print("It is a draw")
 else:
  print("\nThe winner is", winner)
 
def play_again():
 gameplay = input("\nWould you like to play again (Y/N)? ")
 gameplay = gameplay.lower()
 return gameplay 
 
def main():
 valid_play = True
 gameplay = "y"
 welcome()
 player1 = get_player1()
 player2 = get_player2()
 while gameplay == "y":
  p1_play = player1_play(player1)
  valid_play = check_valid_play_p1(p1_play, valid_play)
  while valid_play == False:
   p1_play = player1_play(player1)
   valid_play = check_valid_play_p1(p1_play, valid_play)
  p2_play = player2_play(player2)
  valid_play = check_valid_play_p1(p2_play, valid_play)
  while valid_play == False:
   p2_play = player2_play(player2)
   valid_play = check_valid_play_p1(p2_play, valid_play)
  winner = compare_plays(p1_play, p2_play, player1, player2)
  display_winner(winner)
  gameplay = play_again()
main()
 

 