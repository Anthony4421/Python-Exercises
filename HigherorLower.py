#Higher or Lower
#Anthony Swift

import random

#Welcome player

def welcome():
 print("\nWelcome to the higher or lower game")

#Displays the rules

def rules():
 print("""
  Rules:
  
  You will be shown a sequence of numbers.
  Before the next number is shown you must 
  guess whether the next number is higher
  or lower. If you want to guess higher enter 'H'.
  If you want to guess lower enter 'L'.
  You will start the game with 200 points.
  You will receive 50 points for a correct guess
  and 50 points deducted for a wrong guess.
  Once you reach 500 points you will be given 
  the option to play double or bust. During 
  double or bust if you answer correctly at 
  this point you win. Answer incorrectly 
  you will lose.
   """)


#Ask player to guess if next number is higher or lower
#Change case of guess to upper
#If player does not enter 'H' or 'L'
#ask player to re-enter

def guess_num():
 guess = input("Higher or lower? (H/L) ")
 guess = guess.upper()
 while guess != "H" and guess != "L":
  guess = input("Higher or lower? (H/L) ")
  guess = guess.upper()
 return guess

#Generates first number randomly - the number that is being compared

def generate_number():
 num = random.randint(1,9)
 print("\nThe number is", num)
 return num
 
#Generates second number randomly - the number user has to guess whether is higher or lower
#If this number is the same as the first number (number being compared to)
#then generates another random number

def generate_number2(num):
 num2 = random.randint(1,9)
 while (num2 == num):
  num2 = random.randint(1,9)
 print("\nThe number is", num2)
 return num2

#Checks the choice made by player and displays if they are correct or not
 
def check_guess(guess, num, num2, correct_guess):
 if ((guess == "H") and (num2 > num)) or ((guess == "L") and (num2 < num)) :
  print("\nYou have guessed correctly")
  correct_guess = True
 else:
  print("\nYou guessed incorrectly")
 return correct_guess

#Asks player if they would like to play double or bust
#the first time they reach 500 points
#If player does not enter 'Y' or 'N' 
#asks player to re-enter response

def double_or_bust(score, dob):
 if (score == 500) and (dob == ""):
  dob = input("\nWould you like to play double or bust (Y/N)?")
  dob = dob.upper()
  while dob != "Y" and dob != "N":
   dob = input("Would you like to play double or bust (Y/N)?")
   dob = dob.upper()
 print("\n")
 return dob

#Calculates the score
#If player is playing double or bust:
 #Double the score (to 1000) if correct
 #Zero the score if incorrectly
#Otherwise it is 50 points for a correct guess 
#and 50 points deducted for an incorrect guess

def calculate_score(score, dob, correct_guess):
 if (correct_guess == True):
  if (dob == "Y"):
   score = score +500
  else:
   score = score +50
 else:
  if (dob == "Y"):
   score = score -500
  else:
   score = score -50
   
 return score
 
#Displays message at end of the game
#If the score is 0 displays message to say the game is over
#If the player has reached max points, congratulations message is displayed

def end_game(score):
 if (score == 0):
  print("Game over, you have lost. The game will now end")
 else:
  print("Congratulations you have won. The game will now end")

#Displays the score during each turn

def display_score(score):
 print("Your scores is" ,score)

#Asks player if they would like to play again
#after the game has ended

def get_response():
 response = input("\nWould you like to play again? (Y/N)")
 response = response.upper()
 while response != "Y" and response != "N":
  response = input("Would you like to play again? (Y/N)")
  response = response.upper()
 return response
 
#The main function
 
def gameplay():
 response = "Y"
 while (response == "Y"):
  score = 200
  dob = ""
  welcome()
  rules()
  num = generate_number()
  while (score > 0) and (score < 1000):
   guess = guess_num()
   num2 = generate_number2(num)
   correct_guess = check_guess(guess, num, num2, score)
   score = calculate_score(score, dob, correct_guess)
   display_score(score)
   dob = double_or_bust(score, dob)
   num = num2
  end_game(score)
  response = get_response()
  
gameplay()


 




