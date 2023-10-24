

# ----------------- HEADER --------------------

# This file is a solution to Question 5
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------


from math import ceil, sqrt

# this algorithm finds specified amount of primes
# and adds them do the prime list
count = 2               # indexing for the while loop
number_of_primes = 2    # how many primes have been found so far
prime_list = [2, 3]     # the list of primes found
while number_of_primes < 10001:  # iterate unil reached the specified number of primes
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



# find nth triangular number
def sum_up_to_(n):
    return int(n*(n+1) / 2)

# optimizing code by only calculating factors through prime factors
def count_again(n):
   s = sqrt(n)
   primes = []
   for m in prime_list:
      if m > s:
         break
      if n % m == 0:
         primes.append(m)
    for i in primes:
      
      
# find how many factors n has (very bad code - improve)
def count_factors(n):
    if n == 1:
        return 1
    counter = 1
    for m in range(1, ceil(n / 2) + 1):
        if n % m == 0:
            counter += 1
    return counter

for i in range(1, 1000000):
    if i % 10000 == 0:
        print(i)
    if count_factors(sum_up_to_(i)) > 500:
        print(i)
        quit()