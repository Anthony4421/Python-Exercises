#Football Results Tracker Exercise
#101 Computing - Python Intermediate
#Anthony Swift
#31/03/2020


def menu():
    print("Football Results Tracker: ")
    print("\nMenu: ")
    print("1. Add New Score")
    print("2. Display All Scores")
    print("3. Display Team Scores")
    option = int(input("\nPlease select an option: "))

    return option
     
def add_new_score():

    home_team = input("\nPlease enter the name of the Home team: ")
    away_team = input("Please enter the name of the away team: ")
    home_score = input("Please enter the Home Score: ")
    away_score = input("Please enter the Away Score: ")

    file = open("results.txt","a")
    file.write(home_team)
    file.write(";")
    file.write(away_team)
    file.write(";")
    file.write(home_score)
    file.write(";")
    file.write(away_score)
    file.write(";")
    file.write("\n")
    file.close()

def display_scores():

    file = open("results.txt","r")
    print("\nHome Team – Home Score:Away Score – Away Team")
    print("\n")
    for line in file:
        data = line.split(";")
        print(data[0] + " - " + data[2] + ":" + data[3] + " - " + data[1])

def display_team_scores():
    points = 0
    team = input("Please enter the team name to display all results of the team: ")
    print("\nScores for", team)

    file = open("results.txt", "r")

    for line in file:
        data = line.split(";")
        if data[0] == team:
            print(data[2])
            if data[2] > data[3]:
                points += 3
            elif data[2] == data[3]:
                points += 1
        if data[1] == team:
            print(data[3])
            if data[3] > data[2]:
                points += 3
            elif data[3] == data[2]:
                points += 1
    print("Team", team, "has", points, "points")
            
    
    
    

def main():
    option = menu()
    if option == 1:
        add_new_score()
    if option == 2:
        display_scores()
    if option == 3:
        display_team_scores()
        


main()
                     
                    

                     

    
