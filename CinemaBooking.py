#Cinema Booking Exercise
#Anthony Swift

'''
A cinema booking system for a theatre which consists of 48 seats, organised in 6 rows of 8 seats.
To store information as to whether a seat is booked or available, 
the program uses a 2-dimensional array (in python a list of lists). 
Each cell of the array contains the value 1 if the seat is booked or 0 if it is empty:

The program allows a user to book seats by specifying the row and col number or closest to the front/back
The user can also:
Enter group bookings on consecutive seats
Cancel Bookings
and more...

'''

#Initialises the seats array
#Updates the seats array with what is in the seats text file
#each time the program opens

def initialise_seats():

 seats = [[],[],[],[],[],[]]
 
 #Opens the seats text file
 
 
 file = open("seats.txt","r+")
  
 #Set loop counter to 0
 
 x = 0
  
 #Loops through each line in text file
 #Puts each line in the seats array
 #on the appropriate line number
 
 for line in file:
  line = line.strip()
  line = line.split(",")
  seats[x] = line
   
 #Moves to next line number in seats array
   
  x +=1
	  
 return seats
 
#Display the seats to show the user the which seats booked
 
def display_bookings(seats):

 print("\nBookings:")
 print("\n")

 for x in range(0,len(seats)):
  print(seats[x])

		
#Welcome user to the program
		
def welcome():

 print("\nWelcome to the Cinema Booking Program")

#Displays menu

def menu():
 
 print("\nMenu:")
 print("""
    Option 1: Book a seat by row/column
    Option 2: Book a seat close to the front
    Option 3: Book a seat close to the back
    Option 4: Reset Seats
    Option 5: Cancel Booking
    Option 6: Group Booking close to front
    Option 7: Group Booking close to back
    Option 8: Group Booking by row/column
    Option X: Exit
	""")

#Ask user to select menu option
	
def select_menu_option():
 option = input("\nPlease select an option: ")
 while not (option == "1" or option == "2" or option == "3" or option == "4" or option == "5" or option == "6" or option == "7" or option == "8" or option == "X"):
  print("\nThe option you entered is invalid. Please re-enter")
  option = input("Please select an option: ")
  
 return option
 
 
#Books seat based on the option user has selected

def booking(option,seats,seating_full,group_available):
 
 #If user selected to book seat by row/column
 #Ask user to enter row and col number of seat they would like to book
 
 if option == "1":
  if seating_full == True:
   print("Seating is full. Unable to book seats")
  else:
   row = int(input("\nEnter row number of seat you would like to book: "))
   col = int(input("Enter column number of seat you would like to book: "))
   
 #If the seat booking entered has already been taken or is not in range
 #Keep asking user for row and column number until a free seat is found
 #If seat booking entered hasn't been taken and is in the correct range
 #Books the seat and confirms the booking
   
   while not ((row >= 0 and row <= 5) and (col >=0 and col <=7) and (seats[row][col] == "0")):
    print("\nThe seat entered is not available or invalid")
    row = int(input("\nEnter row number of seat you would like to book: "))
    col = int(input("Enter column number of seat you would like to book: "))
   
   seats[row][col] = "1"
   print("\nThe seat on Row", row, "Column", col,"has been booked")
   

  
 #If the user selects the option to book seat close to front
 #The program loops through the seats array from the start
 #to find the first available seat then books the seat
 #and confirms the booking
 #The flag variable allows both loops to break at the point a seat is found
  
 if option == "2":
  if seating_full == True:
   print("Seating is full. Unable to book seats")
  else: 
   flag = False
   for x in range(0,6):
    for y in range(0,8):
     if seats[x][y] == "0":
      flag = True
      seats[x][y] = "1"
      break
    if flag == True:
     break
   print("\nThe seat on Row", x, "Column", y,"has been booked")
 
 
 #If the user selects the option to book seat close to back
 #The program loops through the seats array backwards from the end
 #to find the first available seat then books the seat
 #and confirms the booking
 #The flag variable allows both loops to break at the point a seat us found
 
 if option == "3":
  if seating_full == True:
   print("Seating is full. Unable to book seats")
  else:
   flag = False
   for x in range(5,-1,-1):
    for y in range(7,-1,-1):
     if seats[x][y] == "0":
      flag = True
      seats[x][y] = "1"
      break
    if flag == True:
     break
   print("\nThe seat on Row", x, "Column", y,"has been booked")
  
 #If the user selects the option to reset seats
 #the program loops through each seat in the seats array
 #and resets the seats the 0
 
  
 if option == "4":
  for x in range(0,6):
   for y in range(0,8):
    seats[x][y] = "0"
  print("All seats have been reset")
  
 #If the user selects the option to cancel a booking
 #Asks the user for row and column number of seat they would like to cancel
 #If the seat the user tries to cancel is already avaiable, lets the user know.
 #Otherwise sets the seat in the seats array to 0
 #Confirms to the user the seat has been cancelled

 
 if option == "5":
  row = int(input("\nEnter row number of seat you would like to cancel: "))
  col = int(input("Enter column number of seat you would like to cancel: "))
  while not ((row >= 0 and row <= 5) and (col >=0 and col <=7)):
   print("\nYou have entered an invalid range for the seating. Please re-enter")
   row = int(input("Enter row number of seat you would like to cancel:"))
   col = int(input("Enter column number of seat you would like to cancel: "))
  if seats[row][col] == "0":
   print("\nThe seat on Row", row, "Column", col,"is already available")
  else:
   seats[row][col] = "0"
   print("\nThe seat on Row", row, "Column", col,"has been cancelled")
 
 #If the user selects the option for a group booking closest to front
 #Asks the user how many people are in the group
 #Loops through the seats array from the start
 #until the program finds consecutive seats for the group that are closest to the front
 #Confirms to the user the seats that have been booked
 #Lets the user know if there are no group bookings avaiable at all / for the total group number specified
 #This was very challenging to code and the logic to get this working is complex
 
 if option == "6":
  total = 0
  if group_available == False:
   print("Group Bookings are full. Unable to book seats")
  else: 
   group_total = int(input("How many people are in the group: "))
   while not (group_total >= 2 and group_total <= 8):
    print("\nYou have entered an invalid group total. Please enter a value from 2 to 8: ")
    group_total = int(input("How many people are in the group: "))
   print("\n")
   flag = False
   for x in range(0,6):
    for y in range(0,8):
     if y == 0:
      total = 0
     if seats[x][y] == "0":
      seats[x][y] = "2"
      total +=1
     if y < 7 and seats[x][y] == "1" and total < group_total:
      for y in range(0,8):
       if seats[x][y] == "2":
        seats[x][y] = "0" 
        total = 0
     if y == 7 and total < group_total:
       for y in range(0,8):
        if seats[x][y] == "2":
         seats[x][y] = "0"
     if total == group_total:
      flag = True
      break
    if flag == True:
     break
   if flag == True:
    for x in range(0,6):
     for y in range(0,8):
      if seats[x][y] == "2":
       print("The seat on row", x,"Column", y,"has been booked")
       seats[x][y] = "1"
   else:
    for x in range(0,6):
     for y in range(0,8):
      if seats[x][y] == "2":
       seats[x][y] = "0"
    print("\nThere are no group bookings available for the group total specified")
	
 #If the user selects the option for a group booking closest to back
 #Asks the user how many people are in the group
 #Loops through the seats array from the end
 #until the program finds consecutive seats for the group that are closest to the back
 #Lets the user know if there are no group bookings avaiable at all / for the total group number specified
 #This was very challenging to code and the logic to get this working is complex
	
 if option == "7":
  total = 0
  if group_available == False:
   print("Group Bookings are full. Unable to book seats")
  else: 
   group_total = int(input("How many people are in the group: "))
   while not (group_total >= 2 and group_total <= 8):
    print("\nYou have entered an invalid group total. Please enter a value from 2 to 8: ")
    group_total = int(input("How many people are in the group: "))
   print("\n")
   flag = False
   for x in range(5,-1,-1):
    for y in range(7,-1,-1):
     if y == 7:
      total = 0
     if seats[x][y] == "0":
      seats[x][y] = "2"
      total +=1
     if y > 0 and seats[x][y] == "1" and total < group_total:
      for y in range(7,-1,-1):
       if seats[x][y] == "2":
        seats[x][y] = "0" 
        total = 0
     if y == 0 and total < group_total:
       for y in range(7,-1,-1):
        if seats[x][y] == "2":
         seats[x][y] = "0"
     if total == group_total:
      flag = True
      break
    if flag == True:
     break
   if flag == True:
    for x in range(5,-1,-1):
     for y in range(7,-1,-1):
      if seats[x][y] == "2":
       print("The seat on row", x,"Column", y,"has been booked")
       seats[x][y] = "1"
   else:
    for x in range(5,-1,-1):
     for y in range(7,-1,-1):
      if seats[x][y] == "2":
       seats[x][y] = "0"
    print("\nThere are no group bookings available for the group total specified")	
	
 #If the user selects the option for a group booking by row
 #Asks the user how many people are in the group
 #Asks the user the row number they would like for the group booking
 #Loops through the seats array from the start of the row specified by user
 #until the program finds consecutive seats for the group that are on the row
 #Confirms to the user the seats that have been booked
 #Lets the user know if there are no group bookings avaiable at all / for the total group number specified / for the row specified

 if option == "8":
  total = 0
  available = False
  if group_available == False:
   print("Group Bookings are full. Unable to book seats")
  else: 
   group_total = int(input("How many people are in the group: "))
   while not (group_total >= 2 and group_total <= 8):
    print("\nYou have entered an invalid group total. Please enter a value from 2 to 8: ")
    group_total = int(input("How many people are in the group: "))
   print("\n")
   while available == False:
    row = int(input("Please enter the row you would like to book: "))
    while not (row >= 0 and row <= 5):
     print("\nYou have entered an invalid row for the seating. Please re-enter")
     row = int(input("Please enter the row you would like to book:"))
    flag = False
    for x in range(0,6):
     for y in range(0,8):
      if y == 0:
       total = 0
      if seats[x][y] == "0" and x == row:
       seats[x][y] = "2"
       total +=1
      if y < 7 and seats[x][y] == "1" and x == row and total < group_total:
       for y in range(0,8):
        if seats[x][y] == "2":
         seats[x][y] = "0" 
         total = 0
      if y == 7 and total < group_total:
        for y in range(0,8):
         if seats[x][y] == "2":
          seats[x][y] = "0"
      if total == group_total:
       flag = True
       break
     if flag == True:
      break
    if flag == True:
     for x in range(0,6):
      for y in range(0,8):
       if seats[x][y] == "2" and x == row:
        print("The seat on row", x,"Column", y,"has been booked")
        available = True
        seats[x][y] = "1"
    else:
     for x in range(0,6):
      for y in range(0,8):
       if seats[x][y] == "2" and x == row:
        seats[x][y] = "0"
     print("\nThere are no group bookings available for the group total on the row specified")
     available = False

	
	

 #If the user selects the option to close the program
 #Closes the program and the contents of the text file
 #are replaced with the contents of the seats array  
  
 if option == "X":
  print("The program will now end")
 
  #Opens the seats text file
 
 
  file = open("seats.txt","w")
  
 #Loops through each element in seats array
 #Puts each element in the text file
 
  for x in range(0,6):
   for y in range(0,8):
    if y == 0 and x !=0:
     file.write("\n")
    file.write(str(seats[x][y]))
    if y != 7:
     file.write(",")
	 
 return seats
	 
#Checks if there are any group bookings available

def check_group_booking_available(seats):

 group_available = False

 for x in range(0,6):
  for y in range(0,7):
   if seats[x][y] == "0" and seats[x][y+1] == "0":
    group_available = True
    break
 return group_available
    

#Counts the number of available seats in the seats array
#and displays to the user
	 
def number_of_seats_left(seats):

 total_seats = 0
 
 for x in range(0,6):
  for y in range(0,8):
   if seats[x][y] == "0":
    total_seats +=1
 print("\nThere are", total_seats,"seats left")
 
 return total_seats
 
#Checks if the seating is full
#Sets seating_full variable to true if seating is full
#and displays message to user to confirm all seats booked

def check_seating_full(total_seats):
 seating_full = False
 if total_seats == 0:
  seating_full = True
  print("All seats have been booked")
 return seating_full

def main():
 option = ""

 seats = initialise_seats()
 welcome()
 while option != "X":
  display_bookings(seats)
  total_seats = number_of_seats_left(seats)
  seating_full = check_seating_full(total_seats)
  group_available = check_group_booking_available(seats)
  menu()
  option = select_menu_option()
  seats = booking(option,seats,seating_full,group_available)

 
main()