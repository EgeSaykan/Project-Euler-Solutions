
# ----------------- HEADER --------------------

# This file is a solution to Question 10
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------


# ------------ WORKING PRINCIPAL --------------

# This file first generates a list of primes
# and adds them up until it reaches 2 million

# it simply check an number is divisible by any
# of the numbers in prime_list
# if it is, then the number is not prime
# if it can't be devided, add it to the list

# ---------------------------------------------



# import square rooting funciton from math library
from math import sqrt


# this algorithm finds specified amount of primes
# and adds them do the prime list
count = 5                       # indexing for the while loop
number_of_primes = 2            # how many primes have been found so far
prime_list = [2, 3]             # the list of primes found
total = 0                       # sum of all prime up to specified one
while True:  # iterate unil interrupted
  prime = True
  for i in prime_list:
    if count % i == 0:
      prime = False
      break
    if sqrt(count) < i:
      break
  if prime:
    if count > 2000000:
      break
    prime_list.append(count)
    total += count
    number_of_primes += 1
  count += 1

print(total + 2 + 3)