#Anagram Game
#Anthony Swift
#05/05/2019

'''
Player will be asked to guess the anagram of 10 words.
For each word the player guesses correctly, they will score 1 point.
'''

import random

#Welcome the player to the game

def welcome():
 print("\nWelcome to the Anagram Game.")
 
def instructions():
  print("""
  You will be asked to guess the anagram of 10 words.
  For each word you guess correctly you will score 1 point.
   """)

#Inserts a list of words from a text file into a list

def initialise_word_list():
 
 wordlist = []
 
 file = open("words.txt","r")
 for line in file:
  line = line.strip()
  wordlist.append(line)
  
 return wordlist

#Picks a word from the word list to be used as the anagram

def pick_word(wordlist):
 word = random.choice(wordlist)
 return word
 
#Scrambles the word
#Randomly picks letters from word picked
#and adds to the anagram variable
#Ensures each letter is only picked once from the word

def scramble_word(word):
 anagram = ""
 pos_taken = []
 for x in range(0, len(word)):
  pos = random.randint(0, len(word)-1)
  while pos in pos_taken:
   pos = random.randint(0, len(word)-1) 
  pos_taken.append(pos)
  anagram += word[pos]
 return anagram
 
#Displays the anagram to the player to be guessed

def display_anagram(anagram):
 print("\nThe anagram is", anagram)
 
#Asks player for their guess

def ask_player_for_word():
 guess = input("\nGuess the Anagram: ")
 guess = guess.upper()
 return guess

#Displays if the player guessed the anagram correctly or not
#Adds 1 to the score if guessed correctly

def display_result(guess, word, score):
 if guess == word:
  print("\nCorrect. You have scored 1 point.")
  score += 1
 else:
  print("\nIncorrect. The correct word is", word)
 print("Your score so far is", score)
 return score

#Displays the final score at the end of the game

def final_score(score):
 print("\nYour final score is", score)

#Asks the player if they would like to play again
#Ends the game if player does not enter 'Y'

def play_again():
 play = input("Would you like to play again?(Y/N): ")
 play = play.upper()
 return play

#The main function

def main():
 play = "Y"
 while play == "Y":
  score = 0
  counter = 0
  welcome()
  instructions()
  wordlist = initialise_word_list()
  while counter < 10:
   word = pick_word(wordlist)
   anagram = scramble_word(word)
   display_anagram(anagram)
   guess = ask_player_for_word()
   score = display_result(guess, word, score)
   counter += 1
  final_score(score)
  play = play_again()
 
 
main()
 
 
 
  

 