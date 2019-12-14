#Prime Numbers upto 9999
#Anthony Swift
#22/05/2019

#List to append prime numbers

nums = []

#Set count to zero

count = 0

#Loops through each number from 1 to 9999
#Works out how many times each number upto the number divides evenly into the number
#Appends number to primes list if only divides evenly twice = by 1 and itself

for num in range(1,100):
 for y in range(1,num+1):
  if y == 1:
   count = 0
  if num%y == 0:
   count +=1
  if count == 2 and y == num:
   nums.append(num)

#Displays the prime numbers to the user

print("\nThe prime numbers from 1 to 9999 are: ")
print("\n")

for elem in nums:
 print(elem)