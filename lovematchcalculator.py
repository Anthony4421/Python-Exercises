#Love Match Calculator
#101 Computing Challenges - Python (Intermediate)
#Anthony Swift
#03/01/2020


'''
For this challenge I will write a program that will prompt the user to enter two first names. 
The program will then calculate and return a Love Match Score based on the following criteria:

Both first names have the same numbers of letters. 	+20 pts
Both first names start with a vowel. 	+10 pts
Both first names start with a consonant. 	+5 pts
Both first names have the same number of vowels. 	+12 pts
Both first names have the same number of consonants. 	+12 pts
Both first names contain at least a “l”, “o”, “v” or “e”. 	+7 pts

For each set of criteria met for both names, the appropriate points will be awarded.

In extreme cases where there are either no vowels or no consonants in both names, 
the same scoring for both first names have the same number of vowels or consonants applies
and 12 points will still be awarded.

If the same letter for a vowel or consonant appears in a name more than once, they still count as multiple occurances
For example, if the letter 'E' appears in a name twice, this counts as two vowels in the name and so on..

'''

#Initialise main variables

def initialise_variables():

 score = 0
 vowel = ['a','e','i','o','u']
 consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
 love = ['l','o','v','e']
 
 return(score, vowel, consonant, love)

#Introduce user to the program

def introduction():

 print("\nWelcome to the Love Match Calculator")
 print("This program will calculate a love match score for two names based on a certain criteria")

#Ask user to enter two first names

def enter_first_names():

 first_name = input("\nPlease enter the first name: ")
 second_name = input("Please enter the second name: ")
 
 #Convert both first names to lower case

 first_name = first_name.lower()
 second_name = second_name.lower()
 
 return(first_name, second_name)

# 1)Checks to see if both first names have the same number of letters
#Adds 20 to the score if this condition is met

def same_number_letters_check(score, first_name, second_name):

 if len(first_name) == len(second_name):
  score +=20
 return(score)

#2) Checks to see if both first names start with a vowel
#Adds 10 to the score if the condition is met

def first_names_start_vowel_check(score, first_name, second_name, vowel):

 if (first_name[0] in vowel) and (second_name[0] in vowel):
  score +=10
 return(score)

#3) Checks to see if both first names start with a consonant
#Adds 5 to the score if the condition is met

def first_names_start_consonant(score, first_name, second_name, consonant):

 if (first_name[0] in consonant) and (second_name[0] in consonant):
  score +=5
 return(score)


#4)Checks to see if both first names have the same number of vowels
#Adds 12 to the score if the condition is met

def same_number_of_vowels_check(score, first_name, second_name, vowel):
 a = 0
 b = 0

 for elem in first_name:
  if elem in vowel:
   a +=1
   
 for elem in second_name:
  if elem in vowel:
   b +=1
   
 if a == b:
  score +=12 
 
 return(score)
  
#5)Checks to see if both first names have the same number of consonants
#Adds 12 to the score if the condition is met

def same_number_of_consonants_check(score, first_name, second_name, consonant):

 a = 0
 b = 0

 for elem in first_name:
  if elem in consonant:
   a +=1
   
 for elem in second_name:
  if elem in consonant:
   b +=1
   
 if a == b:
  score +=12 
 
 return(score)

#6)Checks to see if both first names contains at least a a “l”, “o”, “v” or “e”.
#Adds 7 to the score if the condition is met

def love_letter_check(score, first_name, second_name, love):

 a = 0
 b = 0
 
 for elem in first_name:
  if elem in love:
   a +=1
   
 for elem in second_name:
  if elem in love:
   b +=1
   
 if (a>0) and (b>0):
  score +=7

 return(score)
   
#Displays the final love match score to the user

def display_final_score(score):
 print("\nThe love match score is", score)

 
def main():
 score,vowel,consonant,love = initialise_variables()
 introduction()
 first_name,second_name = enter_first_names()
 score = same_number_letters_check(score, first_name, second_name)
 score = first_names_start_vowel_check(score, first_name, second_name, vowel)
 score = first_names_start_consonant(score, first_name, second_name, consonant)
 score = same_number_of_vowels_check(score, first_name, second_name, vowel)
 score = same_number_of_consonants_check(score, first_name, second_name, consonant)
 score = love_letter_check(score, first_name, second_name, love)
 display_final_score(score)
 
 
main()
 
 
 


 
 

