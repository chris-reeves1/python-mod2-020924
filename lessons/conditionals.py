# if, elif and else
# allows for different pathways for our code to take. 


#my_bool = False

#if my_bool: # condition - if evaluated as true the code will trigger. 
#    print("mybool is true")
#else:
#    print('mybool is false')

#is_admin = False
#is_verifed = False
#on_holiday = False


#if (is_admin or is_verifed) and not on_holiday:
#    print("access granted")
#else:
#    print("access denied")

# if some condition:
    #if some other condition:
        #some code
    #else:
        #some code
# else:
    # some code

# operators:

# equal to: ==
# not equal to: !=
# greater than/greater than or equal to: > / >=
# less than/ less than or equal to: < / <=

#money = 10

#if money >= 10:
#    print("i have some money")
#else:
#    print("not much money")

#temp = 11

#if temp >= 30:
#    print("its very hot")
#elif temp > 25:
#    print("pretty hot")
#elif temp > 15:
#    print("its ok")
#elif temp > 10:
#    print("bad")
#else:
#    print("probably bad")

# exercise:
# user to input a grade/mark
# if the mark is above 85 print distiction
# betweeen 65 and 85 print pass
# anything else print fail.
# use if elif else. 

#x = int(input("enter grade: "))

#if x >= 85: 
#    print("distinction")
#elif x >= 65:
#    print("pass")
#else:
    #print("fail")


# multiple comparators

#deposit = 500
#password = "password1"

#if 0 < deposit < 100 and password == "password1":
#    print(f"thankyou for deposit of {deposit}")
#else:
#    print("deposit failed")

# not

#if not 0 < deposit < 100 and password != "password":
#    print("deposit failed")
#else:
#    print("thanks for depsoit")

# in and not in

#name = "root33"

#if name in ("root", "admin", "user"):
#    print("invalid username")
#else:
#    print("accepted")


#if name not in ("root", "admin", "user"):
#    print("accepted")
#else:
#    print("invalid name")

#exercise:
#weight converter app
#user to input weight
#user to select Kgs or Lbs
#if statement to check the unit entered
#logic to convert the weight (kgs to lbs or lbs to kgs)
#print out the converted value
#error handling for upper/lower case
#optional - error handling for input validation. 


# 1st solution

#weight = float(input("enter weight: ")) 
#unit = input("enter K (kgs) or L (lbs): ")

#if unit.upper() == "K":
#    converted = weight / 0.45
#    print(f"converted weight is {converted}")
#elif unit.upper() == "L":
#    converted = weight * 0.45
#    print(f"converted weight is {converted}")
#else:
#    print("invalid choice - enter L or K !!!!!")

# 2nd solution

#import sys

#try:
#    weight = float(input("enter weight: "))
#except ValueError:
 #   print("invalid input, please enter a numeric value.")
 #   sys.exit() 

#while True:
#    unit = input("enter K (kgs) or L (lbs): ").upper()

#    if unit == "K":
#        converted = weight / 0.45
#        print(f"converted weight is {converted}")
#        break
#    elif unit == "L":
#        converted = weight * 0.45
#        print(f"converted weight is {converted}")
#        break
#    else:
#        print("invalid choice - enter L or K !!!!!")

# highest number

#num = 10
#num1 = 20


# rewrite without using if statements or any in built functions (no max!!!!)

#num = 30
#num1 = 40

#result = num1 + (num - num1) * (num >= num1)

#print(result)



#num = 10
#num1 = 20

#larger = num * (num > num1) + num1 * (num1 > num)
#print(larger)








