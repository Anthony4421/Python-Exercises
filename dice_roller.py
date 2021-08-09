#Dice Roller
#09/08/2021
#Anthony Swift

roll = "Y"

import random

#Ask user how many dice they would like to roll

while roll == "Y":

    total_dice = int(input("\nHow many dice would you like to roll? "))

    #Ask user how many sides each die should have

    total_side = int(input("How many sides should each die have? "))

    #Store rolls

    rolls = []

    #Randomly generate rolls

    for x in range(0,total_dice):
        rolls.append(random.randint(1,total_side))

    #Calculate total of all rolls

    rolls_total = sum(rolls)

    #Display each roll and the total of all rolls

    print("Your rolls were:", str(rolls).replace("[","").replace("]",""),"for a total of", rolls_total)

    #Ask user if they would like to roll again

    roll = input("\nWould you like to roll again? (Y/N): ")
    
    

    
