#Practice Python
#Exercise 18 - Cows and Bulls
#Anthony Swift
#23/05/2019

#Import the random module

import random

#Generate random four digit number
#Ensures the four digit number contains no duplicates

def generate_number():

 number = []

 for x in range(0,4):
  rand = random.randint(0,9)
  while rand in number:
   rand = random.randint(0,9)
  number.append(rand)

 return number
 
#Display number - testing only

def display_number(number):
 for x in range(0,4):
  print(number[x],end="")
  
#Welcome player to the game
  
def welcome():
 print("\nWelcome to the Cows and Bulls Game!")
 
#Ask player for guess
#If player enters a guess not equal to 4 digits 
#or if the guess contains non numeric characters
#or if the guess contains duplicate numbers
#asks player to enter guess again
 
def ask_user_for_guess():

 guess = input("\nEnter a number: ")
 
 duplicate = False
 
 for x in range(0,len(guess)):
  if guess.count(guess[x])>= 2:
   duplicate = True

 while len(guess)!= 4 or guess.isnumeric() == False or duplicate == True:

  print("Invalid guess. Please re-enter")
  guess = input("\nEnter a number: ")
  duplicate = False
  
  for x in range(0,len(guess)):
   if guess.count(guess[x])>= 2:
    duplicate = True
  
 return guess
 
#Checks player guess for total cows (numbers in right place) 
#and bulls (numbers in wrong place)
 
def check_guess(guess, number):
 cows = 0
 bulls = 0
 
 for x in range(0,4):
  if int(guess[x]) == int(number[x]):
   cows +=1
  elif int(guess[x]) in number:
   bulls +=1
   
 return(cows,bulls)
 
#Displays number of cows and bulls to the player
 
def display_cows_and_bulls(cows, bulls):
 print(cows,"cows",bulls,"bulls")
 
#Keeps track of the total guesses
 
def total_guesses(total):
 total +=1
 
 return total
 
#Display how many attempts the player took to guess the number
#at the end of the game

def display_total_guesses(total):

 print("\nYou guess is correct. You took",total,"attempts to guess the correct number")
 
def main():

 cows = 0
 bulls = 0
 total = 0
 
 number = generate_number()
 display_number(number)
 welcome()
 while cows < 4:
  guess = ask_user_for_guess()
  cows, bulls = check_guess(guess, number)
  display_cows_and_bulls(cows, bulls)
  total = total_guesses(total)
 display_total_guesses(total)
 
main()
 

