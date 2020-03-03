#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-7/

'''
code = The largest 3-digit square number.
'''

code = 0

#Used three for loops to loop through individual digits
#from 000 to 999

#Each time the loop goes round
#multiples x by x
#Keeps going until total less than or equal to 999

#Add 1 to code each time the condition is met


#Successfully unlocked the padlock with code 961

for x in range(0,1000):
  total = x * x
  if total <= 999:
   code = total

print(code)