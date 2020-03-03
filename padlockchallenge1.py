#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-1/

code = 0
#Update the code below to solve this challenge

#Loops through the numbers 1 to 40
#Adds the value of x to the code variable
#each time the loop goes round

#Successfully unlocked the padlock with code 820

for i in range(1,41):
 code += i

print("Code:")
print(code)