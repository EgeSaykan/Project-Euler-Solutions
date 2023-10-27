# ----------------- HEADER --------------------

# This file is a solution to Question 13
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------


# ------------ WORKING PRINCIPAL --------------

# reads the numbers from the text file
# store them by splitting them into 10 digit
# numbers (because python integers is limited)

# then add the corresponding parts of numbers
# move the carries to next part of the number
# print out the answer

# ---------------------------------------------




# open the file
f = open("numbers.txt", "r")
array_of_numbres = [] # array of tuple of numbers 
for i, c in enumerate(f.readlines()):

    # read a number than append it to the array by dividing it to 5 different
    # parts because python can't store 50 digit number
    array_of_numbres.append((int(c[:10]), int(c[10: 20]), int(c[20:30]), int(c[30: 40]), int(c[40:50])))
f.close() # close the file after use

# total sum
sums_list = [0 for i in range(5)]

# sum all the numbers in the question
for i in array_of_numbres:
    for m in range(5):
        sums_list[m] += i[m]

# add the carry parts of each extension
for i, c in enumerate(reversed(sums_list[1:])):
    if len(str(c)) > 10:
        sums_list[4-i-1] = sums_list[4-i-1] + int(str(c)[:(len(str(c))-10)])

# print out the first ten digits of the result
if len(str(sums_list[0])) > 10:
    print(str(sums_list[0])[0:10])
else:
    print(sums_list[0])