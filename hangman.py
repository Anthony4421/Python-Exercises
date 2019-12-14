#Practice Python
#Exercise 32 - Hangman
#Anthony Swift
#20/05/2019

import random


#Picks a random word from a file
#Loops through each line in the file
#Appends each word to the words list
#Picks a random word from the words list
#and stores in the word variable

def pick_word():

#List to append the words from the file

 words = []

 file = open("words.txt","r+")
 
 for line in file:
 
  line = line.strip()
  words.append(line)
  
 file.close()
  
 word = random.choice(words)
 print("\n")
 #print word picked for testing purposes
 print(word)
 
 return word
 
#Welcome the player to the game

def welcome():

 print("\nWelcome to Hangman!")

#Displays the letters to the player at start of game
 
def initialise_letters(word):
 
 print("\n")
 print("-" * len(word))

 
#Ask player to guess letter

 
def ask_player_for_guess():

 guess = input("\nGuess your letter: ")
 guess = guess.upper()
 
 return (guess)
 
#Checks the players guess is not blank, numeric
#and that the guess is a single letter
#Otherwise the player is asked to enter guess again
 
def check_guess_valid(guess):

 guess_valid = True
 if guess == "" or len(guess) != 1 or guess.isalpha() == False:
  print("\nYour guess is invalid. Please re-enter")
  guess_valid = False

 
 return guess_valid

#Keeps track of the correct letters guessed

def correct_guessed():
 
 correct = []
 
 return correct
 
#Keeps track of the letters already guessed

def letters_guessed():

 guessed = []
 
 return guessed
 
#Displays the letters to the user after each guess
#Displays the letter if the letter guessed is in the word and stores in letters variable
#Displays '-' if the letter guessed is not in the word and stores in letters variable
#Returns letters variable and ends the game if it matches the word variable
#also checks the correct variable and displays any letters that have already been guessed correctly
 
def display_letters(guess, word, correct, guessed):
 print("\n")
 letters = ""
 for x in range(0,len(word)):
  if word[x] in correct:
   print(word[x],end="")
   letters += word[x]
  elif word[x] == guess:
   print(word[x],end="")
   letters += word[x]
  else:
   print("-",end="")
   letters += "-"
  
 print("\n")

 return (letters)
 
 
#Displays to the user if letter guessed is correct, incorrect or already guessed
#Deducts the number of guesses by 1 if the player gives an incorrect guess
#Appends guess to the guessed variable so the program knows 
#the letter has already been guessed in display letters function
#Appends the guess to the correct variable if the guess was correct 
#so the program knows in the display letters function


def display_result(guess, guessed, word, correct, total_guesses):

 if guess in guessed:
  print("Letter has already been guessed")
 elif guess in word:
  print("Correct!")
  guessed.append(guess)
  correct.append(guess)
 elif guess not in word: 
  print("Incorrect!")
  guessed.append(guess)
  total_guesses -= 1
  
  
 return total_guesses
 
#Displays the total number of guesses remaining to the player
 
def display_total_guesses(total_guesses):
 print("You have",total_guesses,"guesses remaining")
 
#Asks the player if they would like to start a new game when they win or lose

def start_new_game(new_game):
 new_game = input("\nWould you like to start a new game (Y/N): ")
 new_game = new_game.upper()
 return new_game
 
 
#Displays appropriate scaffold based on how many guesses the player has got left

def displayScaffold(total_guesses):

 if total_guesses == 6:
  print("""
          ----------
          |/       |
          |
          |
          | 
          |
         ---
		 
         """)
		 
 if total_guesses == 5:
  print("""
          ----------
          |/       |
          |        0
          |
          | 
          |
         ---
		 
         """)
		 
 if total_guesses == 4:
  print("""
          ----------
          |/       |
          |        0
          |        |
          | 
          |
         ---
		 
         """)
		 
 if total_guesses == 3:
  print("""
          ----------
          |/       |
          |        0
          |       /|
          | 
          |
         ---
		 
         """)
		 
 if total_guesses == 2:
  print("""
          ----------
          |/       |
          |        0
          |       /|/
          | 
          |
         ---
		 
         """)
		 
 if total_guesses == 1:
  print("""
          ----------
          |/       |
          |        0
          |       /|/
          |       /
          |
         ---
		 
         """)
		 
 if total_guesses == 0:
  print("""
          ----------
          |/       |
          |        0
          |       /|/
          |       / /
          |
         ---
		 
         """)
	
#Displays to the player whether they have won or lost at end of game
	
def won_or_lost(total_guesses):
 if total_guesses == 0:
  print("\nYou have lost!")
 else:
  print("\nCongratulations! you have won")
 
 
 
def main():
 new_game = "Y"
 while new_game == "Y":
  total_guesses = 6
  guess_valid = True
  letters = ""
  guess = ""
  word = pick_word()
  welcome()
  initialise_letters(word)
  correct = correct_guessed()
  guessed = letters_guessed()
  while letters != word and total_guesses > 0:
   guess = ask_player_for_guess()
   guess_valid = check_guess_valid(guess)
   while guess_valid == False:
    letters = display_letters(guess, word, correct, guessed)
    displayScaffold(total_guesses)
    display_total_guesses(total_guesses)
    guess = ask_player_for_guess()
    guess_valid = check_guess_valid(guess)
   letters = display_letters(guess, word, correct, guessed)
   total_guesses = display_result(guess, guessed, word, correct, total_guesses)
   displayScaffold(total_guesses)
   display_total_guesses(total_guesses)
  won_or_lost(total_guesses)
  new_game = start_new_game(new_game)
 
 
main()