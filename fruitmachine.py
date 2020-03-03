#101 Computing - Beginner
#Fruit Machine
#Anthony Swift
#06/01/2020

import random

print("\n################################")
print("#                              #")
print("#         Fruit Machine        #")
print("#                              #")
print("################################")
print("")


#Initialise lists for the wheel and results

wheel = ["Banana", "Apple", "Pear", "Cherry", "Watermelon", "Kiwi"]
result = []

#Ask user to spin

enter = input("\nPress enter to spin\n")

print("\n *** Spinning Wheels... *** \n")


#Loops through the wheel list
#Randomly selects three items from the wheel list
#and appends to the results list

for x in range(0,3):
 result.append(random.choice(wheel))

 
#Prints the results to the player

for x in range(0,3): 
 print(result[x]," ",end="")
 
#Checks results to work out if the player has won Jackpot or split
#or has lost
 
print("\n")

if result[0] == result[1] == result[2]:
 print("\nJackpot!")
elif (result[0] == result[1]) or (result[1] == result[2]):
 print("1 Pair!")
elif result[0] == result[2]:
 print("\nSplit!")
else:
 print("\nUnlucky! You lose!")
 
