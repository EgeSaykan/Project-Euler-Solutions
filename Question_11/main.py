# ----------------- HEADER --------------------

# This file is a solution to Question 11
# in Project Euler archives
# (https://projecteuler.net/archives)

# ---------------------------------------------


# ------------ WORKING PRINCIPAL --------------

# firstly the algorithm reads the file with
# numbers and adds each row of numbers to an
# array as an array (so it's a 2D array)

# then it goes through each diognal of 4 and
# multiplies them, stores the greatest value
# in max variable

# then it does the same thing with firstly
# vertical 4, then horizontal 4

# ---------------------------------------------



# open the file
f = open("numbers.txt", "r")
array_of_numbres = [] # array of array of numbers 20x20
for i, c in enumerate(f.readlines()):
    temp = []       # temporary list that stores a row
    temp_str = ""   # temporary string that stores one number to be added to the row

    # iterate through a row of strings
    for p, m in enumerate(c):

        # if m is not [SPACE] then add to temp_str
        if m != " ":
            temp_str += m

        # else, add the temp_str to temp list
        else:
            temp.append(int(temp_str))
            temp_str = ""
        
        # don't forget to add the last number
        if p == len(c) - 1:
            temp.append(int(temp_str))
    
    array_of_numbres.append(temp)
f.close() # close the file after use


max = 1
for i in range(len(array_of_numbres) - 3):
    for k in range(len(array_of_numbres[0]) - 3):
        temp = array_of_numbres[i][k] * array_of_numbres[i+1][k+1] * array_of_numbres[i+2][k+2] * array_of_numbres[i+3][k+3]
        if temp > max:
            max = temp
        temp = array_of_numbres[i+3][k] * array_of_numbres[i+2][k+1] * array_of_numbres[i+1][k+2] * array_of_numbres[i][k+3]
        if temp > max:
            max = temp
for i in range(len(array_of_numbres) - 3):
    for k in range(len(array_of_numbres[0])):
        temp = array_of_numbres[i][k] * array_of_numbres[i+1][k] * array_of_numbres[i+2][k] * array_of_numbres[i+3][k]
        if temp > max:
            max = temp
for i in range(len(array_of_numbres)):
    for k in range(len(array_of_numbres[0]) - 3):
        temp = array_of_numbres[i][k] * array_of_numbres[i][k+1] * array_of_numbres[i][k+2] * array_of_numbres[i][k+3]
        if temp > max:
            max = temp

print(max)

