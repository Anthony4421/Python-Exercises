#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-4/

'''
code = Total number of 3-digit combinations where the sum of 
all three digits (digit1 + digit2 + digit3) is an odd number
'''

code = 0

#Used three for loops to loop through individual digits
#from 000 to 999

#Add the digits each time the loop goes round
#Store the total of the digits in total variable
#Checks to see if total is odd by checking if there is 
#more than one remainder when dividing by 2

#Add 1 to code each time the condition is met


#Successfully unlocked the padlock with code 500

for x in range(0,10):
 for y in range(0,10):
  for z in range(0,10):
   total = 0
   total = x + y + z
   if total%2 > 0:
    code +=1


print(code)