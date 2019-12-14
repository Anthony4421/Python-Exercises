#Practice Python
#Exercise 16 - Password Generator
#Anthony Swift
#18/02/2019

#Import the random module
import random

def initialise_word_list():
 word_list = []
 return word_list

def initialise_password_list():
#Setup list to generated store password
 password = []
 return password

def welcome_user():
 print("\nWelcome to the Password Generator program")
 
def ask_for_password_strength():
 pw_strength = input("\nPlease enter how strong you would like your password to be: (S - Strong) or (W- Weak): ")
 pw_strength = pw_strength.upper()
 return pw_strength

def invalid_password_strength(pw_strength):
 print("\nInvalid selection. Please reenter.")
 
def generate_password(pw_strength, password, word_list):
#If password strength selection is weak
#Picks word from file 
 if pw_strength == 'W':
  file = open("words.txt","r")
  for line in file:
   word_list.append(line)
  password = random.choice(word_list)
  password = password.lower()
 else:
#If password strength is strong
#Randomly selects 8 characters and appends to password list
  for x in range(0,8):
   rand = random.choice('abcdefghijklmnoprstuvwxyz123456789-\/.,?[]{}#~')
  #randomy chooses lower or upper case for current slected character
   case = random.randint(1,2)
   if case == 1:
    rand = rand.lower()
   else:
    rand = rand.upper()
   password.append(str(rand))
 return password

def convert_password_to_string(password):
#Converts password list to a string
 password = ''.join(password)
 return password
 
def display_generated_password(password):
 print("\nGenerated Password: ",password)

def main():
 word_list = initialise_word_list()
 password = initialise_password_list()
 welcome_user()
 pw_strength = ask_for_password_strength()
 while pw_strength !='W' and pw_strength !='S':
  invalid_password_strength(pw_strength)
  pw_strength = ask_for_password_strength()
 password = generate_password(pw_strength, password, word_list)
 password = convert_password_to_string(password)
 display_generated_password(password)
 
main()
  
 
 
 
