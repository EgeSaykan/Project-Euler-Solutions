# ----------------- HEADER --------------------

# This file is a solution to Question 4
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------



# ------------ WORKING PRINCIPAL --------------

# check_palindromic() function takes in a string
# input, if the input has even number of 
# variables it checkes if the string's first
# half is equal to it's second half's reverse
# if the input has odd number of variables
# then just do the same process but ignore the
# middle term

# rest of the code multiples all numbers from a
# variable 'a' to 900 then decrement a 
# by one until either a == 900 or the result
# is found by check_palindromic() function

# ---------------------------------------------


# checks if the given string is a palindromic
def check_palindromic(s):
  if len(s) % 2 == 0:
    if s[:len(s) // 2] == s[len(s) // 2:][::-1]:
      return True
  else:
    if s[:len(s) // 2] == s[len(s) // 2 + 1:][::-1]:
      return True
  return False


# variables that will be multiplied
# to give largest number that's
# product of two 3 digit numbers
a = 999
b = 999

while a > 900:
  result = a * b                    # get the product of current numbers
  result = str(result)              # cast it to string
  if check_palindromic(result):     # check if the result is palindromic
    print(result)
    break                           # stop if the result has been found
  if b > 900:
    b -= 1                          # decrement b by one to get the next result on the next run
  else:
    a -= 1                          # if b is less than 900, reduce a by one as the result will be greater
                                    # and still (probably) unique
    b = a                           # set b to a so b can still be decremented one by one
