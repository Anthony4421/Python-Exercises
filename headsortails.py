#101 Computing - Intermediate
#Heads or Tails
#Anthony Swift
#07/01/2020

'''
In this challenge we will create a game of heads to tails using the following rules:

    The game will consist of 5 rounds.
    In each round:
        the user will make a guess,
        the computer will flip a coin,
        the player will core 1 point for a correct guess.

In order to complete this game we will first create a function called flipCoin() to flip a coin and return the value “Heads” or “Tails”.

Extension Task #1

Can you tweak this code so that the user can only enter the value “Heads” or “Tails” and nothing else. 
(If they do, the program should ask them to re-enter their guess until they enter a valid guess.)

Extension Task #2

Add some code so that when the 5 rounds are over, the user is given the option to either start a new game or to quit.
'''

import random

#Initialise values list

def initialise_values():

 values = ['H','T']
 
 return values
 
#Welcome player to the game
 
def welcome():

 print("\nWelcome to the Heads or Tails game")
 print("The computer will flip a coin")
 print("You must guess if the flipped coin displays heads or tails")
 print("The game will consist of 5 rounds. For each correct guess you will score 1 point")
 
def flip_coin(values):

 result = random.choice(values)
 
 return result
 
#Ask the player for guess
 
def ask_player_for_guess():
 
 guess = input("\nPlease enter your guess (Heads(H) or Tails(T):")
 guess = guess.upper()
 
 return guess
 
#Checks if the guess entered by the player is valid ('H' or 'S')

def check_guess_valid(guess):
 if guess == 'H' or guess == 'T':
  guess_valid = True
 else:
  guess_valid = False
  
 return guess_valid

#Displays the result to the player

def display_result(result):

 print("The computer has flipped the coin")
 print("\nThe result was", result)
 
#Checks if the players guess matches the result of the flipped coin
#Displays to the player if they were correct or not
 
def check_guess(guess, result, score):

 if guess == result:
  print("You guessed correctly. You have scored 1 point")
  score +=1
 else:
  print("You guessed incorrectly") 
  
 return score
 
#Displays final score to the player
 
def final_score(score):

 print("\nYour final score is", score)
 
#Asks player if they would like to start a new game
 
def start_new_game():
 new_game = input("\nWould you like to start a new game? (Y/N): ")
 new_game = new_game.upper()
 
 return(new_game)
 
def check_new_game_choice_valid(new_game):
 
 if new_game == 'Y' or new_game == 'N':
  new_game_choice_valid = True
 else:
  new_game_choice_valid = False

 return new_game_choice_valid
 
 
def main():
 new_game = "Y"
 new_game_choice_valid = True
 while new_game == "Y":
  game_number = 0
  score = 0
  guess_valid = False
  welcome()
  while game_number < 5:
   values = initialise_values()
   result = flip_coin(values)
   guess = ask_player_for_guess()
   guess_valid = check_guess_valid(guess)
   while guess_valid == False:
    print("The guess you entered is not valid. Please re-enter.")
    guess = ask_player_for_guess()
    guess_valid = check_guess_valid(guess)
   display_result(result)
   score = check_guess(guess, result, score)
   game_number +=1
  final_score(score)
  new_game = start_new_game()
  new_game_choice_valid = check_new_game_choice_valid(new_game)
  while new_game_choice_valid == False:
   print("The choice you entered is not valid. Please re-enter")
   new_game = start_new_game()
   new_game_choice_valid = check_new_game_choice_valid(new_game)
 
main()
 
 
 
