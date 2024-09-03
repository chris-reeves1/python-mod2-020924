# iteration is another word for loops.
# repeating blocks of code over and over.
# saves time, avoids duplicating code. 

# 2 types of loops - while/for

# while loops
# a while loop while continuously execute code until a condition is met.
# if the condition the never met the while loop wont stop.
# we have conditions to start a while loop - if not met it wont start. 


#x = 0
#while x < 101:
#    print(x)
#    x += 1

# break 

#i = 1

#while i < 6:
#    print(i)
#    if i == 3:
#        break
#    i += 1

# continue

#j = 0

#while j < 6:
#    j += 1
#    if j == 3:
#        continue
#    print(j)

# while True

#while True:
#    name = input("enter your name: ")
#    if name == "quit":
#        break
#    else:
#        print(f"hello {name}")


# for loops
# a for loop will iterate over a collection - lists/dictionaries/strings etc


# lists

#my_fruits = ["apple", "orange", "kiwi"]
#   # item       # iterable
#for x in my_fruits:
#    print(x)

#numbers = [1, 2, 3, 4]

#for number in numbers:
#    print(number)

#numbers = [1, 2, 3, 4]

#l = 0 
#while l < len(numbers):
#    print(numbers[l])
#    l += 1

# range

#for a in range(5):
 #   print(a)

#for a in range(1,4):
   # print(a)

#for a in range(1, 10, 2):
#    print(a)

# strings

#for letter in "hello":
   # print(letter)

#for word in "hello world".split():
#    print(word)

# list comprehension

    # expression # item  #iterable
#result = [x**2 for x in range(5)]

#print(result)


#result = []

#for x in range(5):
#    result.append(x**2)

#print(results)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                        # expression  # item    # iterable    # condition
#even_squared_numbers = [number**2 for number in numbers if number % 2 == 0]

#print(even_squared_numbers)

# dictionaries

for i in {"drink": "water"}:
    print(i)

for i in {"drink": "water"}.values():
    print(i)

for i in {"drink": "water"}.items():
    print(i)

# nested for loop

#for i in range(1,3):
#    for j in range(1,4):
#        print(i, "x", j, "=", i*j)


# write a loop that takes 5 names and prints the name + is cool. 


# while loop
# for loop
# list comprehsion
# optional - list comp 1 line only !!
































 
