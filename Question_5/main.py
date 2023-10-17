# ----------------- HEADER --------------------

# This file is a solution to Question 4
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------


# ------------ WORKING PRINCIPAL --------------

# This file first generates a list of primes up
# to 100th prime




# import sqrt function
from math import sqrt


# find and list all primes up to and including
# 100th prime in prime_list

# this algorithm goes through each number and
# divides it by all already found primes
# if none of them can divide it perfectly
# then number is a prime and added to prime_list
count = 2
number_of_primes = 2
prime_list = [2, 3]
while number_of_primes < 100:
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
