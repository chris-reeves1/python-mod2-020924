# modules

# libraries - such standard library. Can contain multiple packages and modules.
# Packages - directories of python modules.  
# modules - just python files. 

# many built in and held in memory. Others need to imported. Other also we can install.
# pip - is our package manager. 

# pypi.org

#import math

#number = 10

#answer = math.sqrt(number) # modulename.method(args)

#print(answer)

#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)

#for i in range(5):
#    print(random_pi())

# just with desired objects to save memory

#from math import ceil, floor, pi
#from random import randint

#def random_pi():
 #   return floor(randint(1,20) * pi)

#for i in range(5):
    #print(random_pi())

# exercise:
# Create 2 files, one called dice.py - write a function that will
# generate a random numer between 1 and 6.
# in the second file import the dice module and simulate throwing 2 dice.
# print its result.

# files:
# imortance:
# logs
# stroring and retrieving data
# sharing data
# configs
# running scripts

# read, write, edit(overwriting) files
# most files types are supported. some require importing modules.

# lets focus on txt files:
# read mode ("r") - defualt mode - used for reading a file.
# write mode ("w") - opens a file for editing, creates a  new file is doesnt exist.
# append("a") - opens for writing, will create a file, appends to the end. 

# eg:

#file = open("filename.txt", "mode")

#..... do something


#file.close() # must remeber to close the file, most recently opened closes first. 

# reading from a file:
# read() - read the entire file. 
# readline() - reads a line and moves on to the next line. 
# readlines() - Reads all the line and puts them in a list. 
# seek() - go to a line defualts to line 1. 

# writing to file
# write() - used to a write a string to the file
# writelines() - used to write a list to the file. 

#file = open("lines.txt", "r")

#lines = file.readlines()

#print(lines)

#file = open("lines.txt", "w")

#for n in range(1,11):
 #   newline = "this is a new line" + " " + str(n) + "\n"
 #   file.write(newline)

#file.close()

file = open("lines.txt", "r")

outfile = ""

for line in range(1, 11):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()


file = open("lines.txt", "w")

file.write(outfile)
file.close()

with open("filename.txt", "mode") as file:
    for n in range(1, 10):
        newline = .......
    file.write(newline)
    # we do not need to close the file. 
















































