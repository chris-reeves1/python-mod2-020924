# Variables - a references (a name), a selection of memory (memory location).
# location is protected, can be called/altered/deleted only by name. 

#person_one_age = 30
#x = 30

# naming convention - should be descriptive, lowercase, never start with a number. 
# follow team style and be consistant.  
# pep-8 style guide. 

#1var  = cant start with a number
#Var = capitals are resevered for class names. 
#VAR = constant - just a convention - mneans we do not want the value to change. 
#print = avoid built in python keywors. print_ as workaround. 

# person_one_age = snake_case 
# personOneAge = camelCase  

#scope:

#global_variable = "accessible everywhere"

#def my_function():
#    local_variable = "accessible only inside this function"
#    print(local_variable) # this will work
#    print(global_variable) # this will also work.

#my_function()
#print(local_variable)

# in built functions

#print("prints to standard output")
#input(int('prompts for an input in standard input')) default to a string. 
#type(what is the data type)

#data types:
#x = 10 # int
#y = '10' # str
#z = True/False bools, 1,0 something or nothing. 
#v = 10.25 float - decimal number.

# escape chars

# \ "\hi \t 'you', \n\"hello\" " \n - newline \t - tab \u unicode \U extended unicode

print("person1: \they how are you?\nperson2: \tim good thanks \U0001f604")

# bodmas

# brackets
# order of
# division
# multiplication
# addition
# subtraction

# + - * /
# floor division // 10//3 = 3
# modulo % 10%3 = 1 

# String concatanation
# 

#name = input("what is your name? ")
#age =  int(input("what is your age? "))
#message = "your name is {}, your age is {}".format(name, age)
#print("your name is " + name)
#print("your name is", name, "your age is", age)

#print(f"your name is {name}, your age is {age}")
#print(message)

# string methods

print("HELLO WORLD".lower())
print("hello world".upper())

print("hello world".count("l", 3, -3))

print("hello world world world".replace("world", "class", 2))

print("hello,world".split(","))

















