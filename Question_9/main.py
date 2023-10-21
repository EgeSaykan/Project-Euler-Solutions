
# ----------------- HEADER --------------------

# This file is a solution to Question 8
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------



# ------------ WORKING PRINCIPAL --------------

# perfect_square function squares the input
# compares the integer value of result to 
# result it self
# if they are the same, it returns True
# else, it returns False

# the algorithm loops through 1 to 1000
# every time it loops through a + 1 to 1000
# with each cycle, it calculates c, checks if
# a + b + c == 1000, if so it checks if c
# is a perfect square, if so it prints the
# result

# ---------------------------------------------



from math import sqrt

# returns True if the argument is a perfect square
def perfect_square(c):
    k = sqrt(c)
    return int(k) == k

# loops through the possible numbers
for a in range(1, 1000):
    for b in range(a + 1, 1000):

        # calculates c^2
        temp = a**2 + b**2

        # calculates c
        c = sqrt(temp)

        if a + b + c == 1000:

            # checks if c^2 is a perfect square
            if perfect_square(temp):
                print(int(a*b*c))
