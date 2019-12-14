#My Login Script
#Challenge 5
#Anthony Swift

valid_login = False

#Print header

def print_header():
 print("\nLogin Script: ")

#Ask user if they would like to register an account

def ask_user_for_signup():
 print("\n")
 response = input("Would you like to signup for an account (Y/N)?")
 response = response.upper()
 while response != "Y" and response != "N":
  print("\nInvalid response. Please re-enter.")
  response = input("\nWould you like to signup for an account (Y/N)?")
  response = response.upper()
 return(response)

#Ask user for account details for signup
#If the user leaves any of the fields blank user is requested to enter again

def new_user_signup():
 print("\n")
 firstname = input("Enter you Firstname: ")
 while firstname == "":
  print("\nThe firstname field cannot be left blank. Please re-enter.")
  firstname = input("\nEnter you Firstname: ")
 surname = input("Enter your surname: ")
 while surname == "":
  print("\nThe surname field cannot be left blank. Please re-enter.")
  surname = input("\nEnter your surname: ")
 password = input("Enter password: ")
 while password == "":
  print("\nThe password field cannot be left blank. Please re-enter.")
  password = input("\nEnter password: ")

 return(firstname, surname, password)
 
#Create the username
 
def create_username(firstname, surname):
 number_of_instances = 1
 firstname = firstname.lower()
 surname = surname.lower()
 username = firstname[0] + surname
 
 file = open("usernames.txt","r")
 for line in file:
 #Removes the blanks from the txt file
  line = line.strip()
  for x in range(0,9):
   line = line.strip(str(x))
 #On each line splits the username and passwords into two fields in the txt file
  data = line.split(",")
 #Check how many times the username in the file
 #Adds number to end of the username if it is already in the file
  if username in data[0]:
   number_of_instances +=1
 if number_of_instances > 1:
  username = username + str(number_of_instances)
 return(username)

#Appends the username and password at the end of the file.
#Ensures each entry is put on a new line
#If it is the first user being added on the file does not insert a new line
#The code checks to see if it is the first user added by tracking the line number

def append_user_to_file(username, password):
 line_number = 0
 file = open("usernames.txt","r")
 for line in file:
  line_number +=1
 file.close()
 file = open("usernames.txt","a")
 if line_number > 0:
  file.write("\n")
 file.write(username)
 file.write(",")
 file.write(password)
 file.close()

#Ask for username and password

def get_user_details():
 print("\n")
 user = input("Enter Username: ")
 pw = input("Enter Password: ")
 
 return(user, pw)

#Open the txt file with usernames and passwords
#Loops through each line in the file
#Checks to see if username password entered is valid and sets valid_login flag

def check_file(user, pw):
 valid_login = False
 file = open("usernames.txt","r")
 for line in file:
 #Removes the blanks from the txt file
  line = line.strip()
 #On each line splits the username and passwords into two fields in the txt file
  data = line.split(",")
 
  if (user == data[0]) and (pw == data[1]):
   valid_login = True
 file.close()
 return(valid_login)
 
#Tracks number of login attempts
 
def number_of_attempts(attempts):
 attempts +=1
 return(attempts)

#Checks if user login is valid and displays appropriate message

def display_valid_login(valid_login):
 if valid_login == True:
  print("\nYou are logged in")
 else:
  print("\nIncorrect login details")

#This is checked at the end of the program
#If the valid login flag is still false
#Display message to let player know maximum attempts exceeded

def check_max_login_attempts(valid_login):

 if valid_login == False:
  print("Maximum attempts exceeded. The program will now end.")
  
#Asks user if they would like to change their password
  
def ask_user_change_password():
 print("\n")
 response = input("Would you like to change your password (Y/N)?")
 response = response.upper()
 while response != "Y" and response != "N":
  print("\nInvalid response. Please re-enter.")
  response = input("\nWould you like to change your password (Y/N)?")
  response = response.upper()
 return(response)
 
#Asks user for new password
#Checks to see if passwords match
#Asks user to enter again if passwords do not match or password entered is blank
 
def ask_user_for_new_password():
 password = input("\nPlease enter new password: ")
 while password == "":
  print("Password cannot be left blank. Please re-enter")
  password = input("\nPlease enter new password: ") 
 password_check = input("Please enter new password: ")
 while password != password_check:
  print("\nThe password's do not match. Please re-enter.")
  password = input("\nPlease enter new password: ")
  while password == "":
   print("Password cannot be left blank. Please re-enter")
   password = input("\nPlease enter new password: ") 
  password_check = input("Please enter new password: ")
 return(password)

#Updates password when user changes it.
#Reads through file and stores all usernames and passwords in a list
#Except the username of the password that is being changed
#Wipes the file
#Writes all usernames and passwords from list into clean file
#Appends username and password being changed to the end of the file

def update_password(user, password, pw):
#Store all usernames in list to append to new file
 list = []

 file = open("usernames.txt","r")
 for line in file:
  data = line.split(",")
  line = line.strip()
  if data[0] != user:
   list.append(line)
 file.close() 
#Wipes current file
 file = open("usernames.txt","w")
 file.close()
#Appends usernames from list to new file
 file = open("usernames.txt","a")
 for item in list:
  file.write(item)
  file.write("\n")
 #file.write("\n")
 file.write(user)
 file.write(",")
 file.write(password)
 file.close()
 


def main():
 attempts = 0
 print_header()
 response = ask_user_for_signup()
 if response == "Y":
  firstname, surname, password = new_user_signup()
  username = create_username(firstname, surname)
  append_user_to_file(username, password)
 user, pw = get_user_details()
 attempts = number_of_attempts(attempts)
 valid_login = check_file(user, pw)
 display_valid_login(valid_login)
 while attempts < 3 and valid_login == False:
  user, pw = get_user_details()
  attempts = number_of_attempts(attempts)
  valid_login = check_file(user, pw)
  display_valid_login(valid_login)
 if valid_login == True:
  response = ask_user_change_password()
  if response == "Y":
   password = ask_user_for_new_password()
   update_password(user, password, pw)
 check_max_login_attempts(valid_login)
 
 
main()
 
 
 
 
 
 




