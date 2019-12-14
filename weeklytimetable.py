#Weekly Timetable Exercise
#Anthony Swift
#22/05/2019

#Stores the timetable

def initialise_timetable():

 timetable = [['History','Maths','Computer Science','PE','Music'],
              ['English','Spanish','Maths','Geography','Art'],
			  ['PE','English','Science','Art','PE'],
			  ['Maths','English','Philosophy','Spanish','Music'],
			  ['Science','Drama','History','Geography','Science']]
			  
 return timetable
 
def welcome():
 print("\nWelcome to the Weekly Timetable program")
 
#Displays the menu of options to the user
 
def menu():

 print("\nMenu:")
 print("""
    Option 1: What Lesson?
    Option 2: Today's Lessons?
    Option 3: How Many Lessons?
	""")
 
#Ask user to select menu option
	
def select_menu_option():
 option = int(input("\nPlease select an option: "))
  
 return option
 
#Asks user to enter day of the week and period of the day
#Retrieves and outputs the lesson on that day and period

def what_lesson(timetable):
 
 day = input("\nPlease input a day of the week (Monday - Friday): ")
 period = int(input("Enter a period of the day (between 1 and 5): "))
 period -=1
 
 if day == "Monday":
  lesson = timetable[0][period]
 elif day == "Tuesday":
  lesson = timetable[1][period]
 elif day == "Wednesday":
  lesson = timetable[2][period]
 elif day == "Thursday":
  lesson = timetable[3][period] 
 elif day == "Friday":
  lesson = timetable[4][period] 

 
  
 print("\nThe lesson is", lesson)
 
#Asks user to enter day of the week
#Displays all five lessons for that day
 
def todays_lessons(timetable):

 day = input("\nPlease input a day of the week (Monday - Friday): ")
 print("\nThe lessons for the day entered are: ")
 print("\n")
 
 for y in range(0,5):
  if day == "Monday":
   print(timetable[0][y])
  elif day == "Tuesday":
   print(timetable[1][y])
  elif day == "Wednesday":
   print(timetable[2][y])
  elif day == "Thursday":
   print(timetable[3][y])
  elif day == "Friday":
   print(timetable[4][y])
   
#Asks the user to enter a subject
#Counts and outputs the number of lessons for that subject throughout the week
   
def how_many_lessons(timetable):

 count = 0

 subject = input("\nPlease enter a subject: ")
 
 for x in range(0,5):
  for y in range(0,5):
   if timetable[x][y] == subject:
    count += 1
	
 print("You have", count, subject,"lessons this week")
 



  
 
 
 
def main():

 timetable = initialise_timetable()
 welcome()
 menu()
 option = select_menu_option()
 if option == 1:
  what_lesson(timetable)
 if option == 2:
  todays_lessons(timetable)
 if option == 3:
  how_many_lessons(timetable)
  
 
main()
			 
 
			 