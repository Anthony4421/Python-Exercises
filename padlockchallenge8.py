
#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-8/

'''
code = The largest 3-digit prime number.
'''

code = 0

#Successfully unlocked the padlock with code 997

for x in range(999,0,-1):
 #set number of divisors to 0 
 #at start of checking each number
 divs = 0
 #Checks how many numbers between 1 and 999
 #are a divisor of x
 for y in range(1,999):
  if x%y == 0:
   divs += 1
 #sets code to number in prime list
 #if number only has 2 primes (1 and itself)
 if divs == 2:
  code += x
  break
  #breaks out of both loops as soon as prime number closest
  #to 999 is found
 
#Outputs 997 - the highest prime found
  
print(code)
  

   
 
 



 
 