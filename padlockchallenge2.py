#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/

code = 0

#Used three for loops to loop through individual digits
#from 000 to 999
#used if statement to check if digit 1 less than 2 
#and digit 2 less than 3
#Add 1 to code each time the condition is met

#Successfully unlocked the padlock with code 120

for x in range(0,10):
 for y in range(0,10):
  for z in range(0,10):
   if (x < y) and (y < z):
    code +=1

print(code)

 


 
 