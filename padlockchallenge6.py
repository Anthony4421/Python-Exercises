#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-6/

'''
code = Total number of 3-digit combinations 
where one digit is equal to the sum of the other two digits.
'''

code = 0

#Used three for loops to loop through individual digits
#from 000 to 999

#Compares x,y and z to see if either are equal to sum of other two digits

#Add 1 to code each time the condition is met


#Successfully unlocked the padlock with code 136

for x in range(0,10):
 for y in range(0,10):
  for z in range(0,10):
   if (x == y+z) or (y == z+x) or (z == x+y):
    code +=1


print(code)