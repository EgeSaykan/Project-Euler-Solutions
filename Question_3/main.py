# ----------------- HEADER --------------------

# This file is a solution to Question 3
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------



# ------------ WORKING PRINCIPAL --------------

# This file first generates a list of primes up
# to 9601st prime
# optimally more primes is needed, but I know
# for a fact that given number in the question
# is not a perfect square
# so 9601 is enough number of primes

# then it goes through every number that is less
# than square root of given number in question
# to check if it is a factor and also prime

# ---------------------------------------------




# import square rooting funciton from math library
from math import sqrt


# this algorithm finds specified amount of primes
# and adds them do the prime list
count = 2               # indexing for the while loop
number_of_primes = 2    # how many primes have been found so far
prime_list = [2, 3]     # the list of primes found
while number_of_primes < 9601:  # iterate unil reached the specified number of primes
  prime = True
  for i in prime_list:
    if count % i == 0:
      prime = False
      break
    if sqrt(count) < i:
      break
  if prime:
    prime_list.append(count)
    number_of_primes += 1
  count += 1


num = 600851475143              # number to get the highest prime factor of
run = True                      # keep running until biggest prime factor is found
biggest = round(sqrt(num))      # current number to be checked if it is a factor and prime
while run:
  if num % biggest == 0:        # if current number is a factor number in the question, 
    if biggest in prime_list:   # if the number is a prime as well,
      run = False               # stop the program
      break
  biggest -= 1                  # decrement biggest to go through all numbers before sqrt of number in the question

print(biggest)                  # print given result
