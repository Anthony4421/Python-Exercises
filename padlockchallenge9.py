
#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-9/

'''
code = The average of all prime numbers 
between 0 and 999 (rounded to the nearest value).
'''
code = 0
total_number_of_primes = 0
total_of_primes = 0

primes = []

#Successfully unlocked the padlock with code 453

for x in range(1,1000):
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
 #append x to primes list
 #Add 1 to total vairable
 if divs == 2:
  primes.append(x)
  total_number_of_primes +=1

#Loops through prime list
#Adds each element to total_of_primes list
#Works out the average by multiplying the total of total_primes_list
#by how many primes there are (total_number of_primes)

for x in range(0,len(primes)):
 total_of_primes += primes[x]
 
code = (total_of_primes / total_number_of_primes)
 
#Outputs 453 - the average of all primes
print(code)