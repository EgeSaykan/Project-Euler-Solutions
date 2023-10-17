# ----------------- HEADER --------------------

# This file is a solution to Question 6
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------

x = 100
print(int((x * (x + 1) / 2)**2 - sum([i**2 for i in range(x + 1)])))