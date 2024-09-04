# collections are our complex data types. 
# different ways of mstoring our data. 

# lists - ordered(indexed), mutable, collection of values -
# [a{index position 0}, b{index position 1}, c{index position 2/-1}]
# 
# dictionaries - unordered(no index positions), mutable, collection of key:pair values.
# {key: pair, key1: value, key2: value}
# 
# tuples - ordered, immutable (cant be altered), collection of values (a, b , c)
# or no brackets at all. x = 1, 2, 3 
#
# sets - unordered, mutable, collection of unique values, - {a, b, c}


#lists:

# lists are stored in []

#colours = ["blue", "red", "yellow", "orange"]

#print(colours)

# direct access

#print(colours[0])
#print(colours[3])
#print(colours[-2])

# slicing: create a sub list up to but not including the 2nd number.

#print(colours[0:2]) # blue and red
#print(colours[1: ]) # no second number slices to the end.

# altering a list with direct access

#food = ["rice", "pasta", "apple", "bread"]

#print(food)
#food[0] = "pizza"
#print(food)

#del food[1]
#print(food)

# nested lists

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# string methods

# append

#my_fruits = ["apple", "orange", "pear"]

#my_fruits.append("kiwi")

#print(my_fruits)

# remove 

#my_fruits.remove("apple")
#print(my_fruits)

# insert 

#my_fruits.insert(0, "mango")
#my_fruits.insert(0, "grapes")
#print(my_fruits)

# extend

#my_fruits.extend(["melon", "blueberry"])
#print(my_fruits)

# reveres

#my_fruits.reverse()
#print(my_fruits)

# sort 

#my_fruits.sort()
#print(my_fruits)

#my_fruits.sort(key=len)
#print(my_fruits)

# join

#x = "#".join(my_fruits)#
#print(x)

# dictionaries
# {} key:value pairs

# no indexing. 
# keys unique values can be anything.

#d#rinks = {"fizzy": "sprite", "still": "water", "juice": "orange", "alcoholic": "wine"}

#print(drinks)

# direct access
#
#print(drinks["still"])

#drinks["non-alcohlic"] = "water"
#print(drinks)

#drinks["non-alcohlic"] = "squash"
#print(drinks)

# methods

# values/keys/items

#print(drinks.values())
#print(drinks.keys())
#print(drinks.items())

# get method

#print(drinks.get("still"))
#print(drinks.get("stille"))
#print(drinks.get("stille", "not-found"))

# update 

#drinks.update({"sugery": "cola"})
#print(drinks)

# pop

#print(drinks.pop("non-alcohlic"))
#print(drinks)

# exercise:

#make a dictionary of books, with 3 authors and multiple books per author.
#have an input that asks for an author name.
#print a STRING of books by that author (NOT A LIST!!). use join. 
#optionally have a little bit of error handling for incorrect author names, using a method. 

#books = {"author1": ["book1", "book2"], "author2": ["book3", "book4"]}

#x = input("enter an author name: ")

#print(", ".join(books[x]))

# 2nd solution

#y = input("enter author name: ")

#x = books.get(y, [])

#print(", ".join(x) or "author not found")

# tuples
# similar to lists but immutable. 
# indicates we donbt to change the data. 
# more speed - very slight
# less memory -  very slight


# use () or no brackets at all

#rectangle = 10, 5

#rectangle[0] = 15

# tuple methods just count and index.
# built in functions also like zip, max, len, min etc...

# sets

# no indexing, unique values.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union - combines sets removes duplicates.
print(set1.union(set2))

# intersection

print(set1.intersection(set2))

# difference

print(set1.difference(set2))

# symetircal diff

print(set1.symmetric_difference(set2))










