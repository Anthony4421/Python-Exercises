#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-3/

code = 0

#Used three for loops to loop through individual digits
#from 000 to 999
#Checked each digit to see if they have no divisors
#if divisable by two to determine if they are all even
#Add 1 to code each time the condition is met


#Successfully unlocked the padlock with code 125

for x in range(0,10):
 for y in range(0,10):
  for z in range(0,10):
   if (x%2 == 0) and (y%2 == 0) and (z%2 == 0):
    code +=1

print(code)
