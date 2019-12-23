#Assignment 5 - Quiz
#Anthony Swift
import random

def welcome():

#Welcome player to the quiz

 print("\nWelcome to the Soaps Quiz.")
 print("\nThis quiz will determine if you are a real soap addict!")
 
def ask_user_for_name():

#Ask player for name
 
 name = input("\nWhat is your name? ")
 
 return(name)
 
def greet_user(name):

#Greet the user by their name
 
 print("\nHi,", name)
 
def quiz_categories():

#Setup the quiz categories in a list
#This is used when checking to see if there are questions in the player's favourite category

 categories = ["Emmerdale","Eastenders","Corrie"]
 
 return(categories)


 
def ask_for_favourite_soap():

#Ask player for their favourite soap
#Capitalize to match format in the list

 fav_soap = input("\nWhat is your favourite soap opera? ")
 fav_soap = fav_soap.capitalize()
 
 return(fav_soap)
 
def display_if_fav_soap_in_quiz(fav_soap,categories):

#If the favourite soap the player entered is in the categories list
 if fav_soap in categories:
  print("\nLucky you! There are", fav_soap, "questions in this quiz")
 else:
#If the favourite soap the player entered is not in the categories list
  print("\nSorry, there are no", fav_soap, "questions in this quiz")
  

 
def display_questions(question,asked):

#Opens the txt file which contains the questions and displays each question to the player
#Displays the relevant question based on the line number.
 
 file = open("myquizquestions.txt")
 line_number = 0
 
 for line in file:
  if line_number == 8 * question or line_number == 8 * question + 1:
   print("\n",line)
  if line_number == 8 * question + 2:
   print("\n 1 -",line)
  elif line_number == 8 * question + 3:
   print("\n 2 -",line)
  elif line_number == 8 * question + 4:
   print("\n 3 -",line)
  elif line_number == 8 * question + 5:
   print("\n 4 -",line)
    
 
  line_number +=1
 print(asked) 
def ask_user_for_answer():

#Ask user for answer to question

 answer = input("\nChoose your answer: ")
 
 return(answer)
 

def check_answer(answer, question):

#Checks the answer player has given to the question.
#Looks at the line number on the file where the answer is displayed
#Checks to see if the answer player has given is on the line.
#Sets correct flag to True if the answer is correct 
#Sets the correct flag to False if the answer is incorrect.

 line_number = 0
 correct = False

 file = open("myquizquestions.txt","r")

 for line in file:
  
  if line_number == 8 * question + 6:
   if str(answer) in line and str(answer) !="":
    correct = True
   else:
    correct = False
  line_number +=1
 return(correct)
 
 
def display_answer(correct,question):

#Finds the line number in the file that shows the message with the correct answer
#Displays whether the player has answered correctly or not
#Displays the message with the correct answer
 line_number = 0

 file = open("myquizquestions.txt","r")
 
 for line in file:
  line_number +=1
  if line_number == 8 * question + 8:
   if correct == True: 
    print("\nCorrect!,",line)
   else:
    print("\nIncorrect!,",line)
	
def calculate_score(correct,score):

#Each time player gives a correct answer to a question adds one to the score
 if correct == True:
  score +=1
 return(score)
  
def display_score(score,question_number):

#Displays the score from number of questions answered
 print("\nScore:", score, "from", question_number+1)
	
def track_question_number(question_number):

#Tracks the current question number
#This is used to determine the correct line numbers when displaying each question block.
#and to determine the number of questions answered when showing scores
 question_number +=1

 return(question_number) 
 
def asked_question_numbers():
 asked = []
 return(asked)

def select_question(asked,total_questions):
 question = random.randint(0,total_questions-1)
 while question in asked:
  question = random.randint(0,total_questions-1)
 asked.append(question)
 return(question)
 
def final_score(score,question_number):

#Displays final score at end of the game

 print("\nYour final score is" ,score, "from", question_number+1)
 
def last_question_message():

#Displays message after last question

 print("\nThat was the last question")
 
def calculate_total_num_questions():
 total_lines = 0
 file = open("myquizquestions.txt","r")
 for line in file:
  total_lines +=1
 total_questions = total_lines / 8
 return(total_questions)
 
def display_total_num_questions(total_questions):
 print("There are", int(total_questions), "questions in this quiz")

def main():
#Main function

 correct = False
 question_number = 0
 score = 0
 welcome()
 name = ask_user_for_name()
 greet_user(name)
 categories = quiz_categories()
 fav_soap = ask_for_favourite_soap()
 display_if_fav_soap_in_quiz(fav_soap, categories)
 asked = asked_question_numbers()
 total_questions = calculate_total_num_questions()
 display_total_num_questions(total_questions)
 while question_number < total_questions:
#Loop - while the question number is less than 5
#the game is in progress
  question = select_question(asked,total_questions)
  display_questions(question, asked)
  answer = ask_user_for_answer()
  correct = check_answer(answer,question)
  score = calculate_score(correct,score)
  display_answer(correct,question)
  display_score(score,question_number)
  if question_number == total_questions - 1:
  #If last question has been answered
  #Display message and final score
   last_question_message()
   final_score(score,question_number)
  question_number = track_question_number(question_number)
  
 
main()
