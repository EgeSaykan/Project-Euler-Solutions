

# ----------------- HEADER --------------------

# This file is a solution to Question 12
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------


# ------------ WORKING PRINCIPAL --------------

# This file first generates a list of primes up
# to 1001st prime

# check_factors checks how many factors argument
# has 
# it iterates through primes in primes list and
# see if the prime is a factor of remaining
# if so it divides the number until it cannot be
# divided anymore

# then it calculates all the possible 
# combinations of multipications of the
# primes and returns length of the set

# ---------------------------------------------



from math import ceil, sqrt

# this algorithm finds specified amount of primes
# and adds them do the prime list
count = 2               # indexing for the while loop
number_of_primes = 5    # how many primes have been found so far
prime_list = [2, 3]     # the list of primes found
while number_of_primes < 1001:  # iterate unil reached the specified number of primes
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

# returns how many factors argument has
def count_factors(n):

  # adds all prime factors to primes list
  primes = []
  temp = n
  for m in prime_list:
    if m > ceil(n / 2):
        break
    if n % m == 0:
      while temp % m == 0 and temp != 0:
        primes.append(m)
        temp = temp / m
  
  # multiplies all combination of primes list
  result = [1]
  for p in primes:
        result += [x * p for x in result]
  return len(set(result))

# iterate through all triangular numbers until one has over 500 factors
for i in range(1, 20000):
    if count_factors(sum_up_to_(i)) > 500:
        print(sum_up_to_(i))
        break