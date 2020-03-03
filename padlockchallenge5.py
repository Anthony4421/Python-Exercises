#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-5/

'''
code = Total number of 3-digit combinations 
where at least two digits are equal.
'''

code = 0

#Used three for loops to loop through individual digits
#from 000 to 999

#Compares x,y and z to see if at least two are equal
#each time the loop goes round

#Add 1 to code each time the condition is met


#Successfully unlocked the padlock with code 280

for x in range(0,10):
 for y in range(0,10):
  for z in range(0,10):
   if (x == y) or (y == z) or (x == z):
    code +=1


print(code)