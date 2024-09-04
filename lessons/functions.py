# functions - a block of code - either going to perform a task or return a value.
# repeatability. 

#def greet(name): # parameters take in arguments
#    print(f"hello {name}")

#greet("chris")

#def greet_1(first_name, second_name, age):
#    print(f"{first_name} {second_name} is {age}")

#greet_1("john", "smith", 30)

# print and input limit functionality. 
# better to store output in a variable or file

# return

#def greeter(name):
#    return f"hello {name}"

#x = greeter("chris")

#print(x)

# default values

#def greet_3(name, age=10): # defaults have to come at end of line.
#    return f"{name} is {age}"

#print(greet_3("chris"))
#print(greet_3("chris", 20))

# *args
# used for when we do not know how many arguments need to be passed through.
# Receive a tuple of args. 

#def fruit_list(*fruits):
#    print("the fruits are: ")
#    for fruit in fruits:
#        print(fruit)

#fruit_list("orange", "apple", "pear")

#def numbers_list(*numbers):
#    for i in numbers:
#        print(i)

#numbers_list(1, 2, 3, 4, 5, 6, 7)

#def make_pizza(size, *toppings):
 #   print(f"order for {size}-inch pizza with the following topping:")
 #   for topping in toppings:
 #       print(topping)

#make_pizza(12, "mushrooms", "peppers")

# kwargs- keyword args
# order does not matter as
# send args as key:value pairs

#def fruit_list(fruit1, fruit2, fruit3):
 #   print(f"fav is {fruit1}")
  #  print(f"2nd fav is {fruit2}")
   # print(f"3rd fav is {fruit3}")#

#fruit_list(fruit3="apple", fruit1="pear", fruit2="orange")

# **kwargs
# if we dont know how many kwargs will be passed through.

#def fav_food(**food):
#    print("fav food is", food['dessert'], "not", food['dairy'])

#fav_food(dessert="ice cream", fruit="apple", dairy="milk")

# combined *aqrgs and **kwargs

#def combine(*args, **kwargs):
  #  print("args: ", args)
 #   print("kwargs: ", kwargs)

#combine(1, 2, 3, a=5, b=10)

# / 
# / is a positional marker 
# introduced in python 3.8
# befrore / is positional args only
# after is keywords. 
# * everyhtin after must be keyword. 

#def example(a, b, /, c, d):
 #   print(f"a = {a}, b = {b}, c = {c}, d = {d}")

#example("a", "b", d="d", c="c")

#def maths_operation(a, b, /, operation="add", *, decimal_place=2):
#    if operation == "add":
#        result = a + b
#    elif operation == "subtract":
#        result = a - b
#    else:
#        raise ValueError("invalid operation")
#    return round(result, decimal_place)

#print(maths_operation(10, 5))
#print(maths_operation(10, 5, operation="subtract"))
#print(maths_operation(10.2255, 5.5522446, operation="add"))


# passing a list to a function

#def my_function(food):
 #   for x in food:
#        print(x)

#my_list = ["apple", "pear", "orange"]

#my_function(my_list)

# type annotations

# allow us to specify the expected data types. 
# introduced 3.5
# not checked or enforced at run time. 


#def greet(name: str) -> str:
    #return f"hello {name}"

# recurrsion

#def factorial(n):
    #if n == 1:
   #     return 1
  #  else:
 #       return n * factorial(n - 1)

#print(factorial(5))

# lambda functions
# lambda argument: expression (iterable)
# short, unnamed functions, calculate a single expression. 

#def add(x, y):
#    return x + y

#add_lambda = lambda x, y: x + y 

#print(add(2, 4))
#print(add_lambda(2, 4))

numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))

# higher-order functions
# functions that either take another function as an argument or return a
# function - or both. 

def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

print(apply_function(square, 5))

# avoids duplication
# modularisation















































































