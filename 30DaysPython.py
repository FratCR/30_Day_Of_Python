# 30 Days of Python Lessons

# Start of Day 1

# DATA TYPES

"""
print(type(18))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Firat'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Firat'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
"""

# OPERATORS
"""
# we can use 3 nail to the area we don't want it to detect
addition(+)
subtraction(-)
multiplication(*)
division(/)
exponential(**)
modulus(%)
Floor division operator(//)
"""
# End of the Day 1

# --------------------

# Start of the Day 2

# variable names must not start with numbers or special characters or '-' character
# No spaces when naming a variable

"""
number1, string1, float1 = 13, "Hi Guys", 2.69 # you can add multiple value in 1 line
print("Firat saying: ", string1)

name, age = input("What is your name ? "), input("What is your age ? ") # you can want user input and you can add multiple in 1 line again
print(f"Hello {name}! Welcome to our store. Your age is {age}, right huh {name} ?")
"""

# CONVERT TYPES

# int to float

"""
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to float
num_str = '10.6'      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Firat'
print(first_name) # 'Firat'
first_name_to_list = list(first_name)
print(first_name_to_list) # ['F', 'i', 'r', 'a', 't']
"""

# End of the Day 2

# -------------------

# Start of the Day 3

# PYTHON OPERATORS

"""
Operator	Example	    Same As	
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=	        x >>= 3	    x = x >> 3	
<<=	        x <<= 3	    x = x << 3
"""

"""
Operator	Name	                    Example
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y
"""

"""
Operator	Description	                                                Example
and 	    Returns True if both statements are true	                x < 5 and  x < 10	
or	        Returns True if one of the statements is true	            x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)
"""

"""
# Homework 1: Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
print("Calculate the area of the triangle by entering the base area and height values (cm)")
basearea = float(input(" Enter a Base area: "))
height = float(input("Enter a Height: "))
triangleArea = (basearea * height)/2
print(f"Your Triangle area is {triangleArea} santimeters...")

# Homework 2: Find the length of 'python' and 'dragon' and make a falsy comparison statement

print(len("Python") == len("Dragon")) == False

# Homework 3: Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person

print("Enter your hourly money earnings and work hours, let's find your weekly and monthly earnings")
Rph = float(input("Enter your rate per hour: "))
daily_work = float(input("Enter your daily work hour as dollar: "))
daily_earn = (Rph * daily_work)
print("Your weekly earned money is: ", daily_earn * 7," USD$")
print("Your montly earned money is: ", daily_earn * 30, " USD$")
"""

# End of the Day 3

# -----------------

# Start of the Day 4

# STRINGS

"""
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
"""

# STRING FORMATS
"""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
"""
#Example

"""
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
"""

# Python 3 new "format" method in strings

"""
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
"""

# Python 3.6 new "f" method in string

"""
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
"""

# Python index numbering

"""
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
"""

# Slicing Python Strings

"""
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
"""

# STRING METHODS

"""
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

challenge = 'thirty days of python'
print(challenge.find('y'))  # 16
print(challenge.find('th')) # 17

challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 5
print(challenge.rfind('th')) # 1

first_name = 'Firat'
last_name = 'Cakir'
age = 18
job = 'Student'
country = 'Turkey'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Firat Cakir. I am 18 years old. I am a Student. I live in Turkey.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
"""

# End of the Day 4

#-------------------

# Start of the Day 5

# LISTS

# 2 Type of Create a Lists

""""
empty_list1 = list()
empty_list2 = []

print(len(empty_list1)) # 0 because empty
print(len(empty_list2)) # 0 because empty too

# lists can contain anything of both desired and desired type

list_numbers = [1,2,3,4,5,6,7,8,9]
list_variable = [1,2,"Hi", False, 3.14, 5.16, "Guys"]

print(list_numbers, list_variable)

# you can take anything in the list with index numbers or you can asign these
#  you can take or go with the negative index numbers, they are going reverse in the list
"""

"""
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
"""

# you can apply, change or delete anything inside of lists

# LIST METHODS

list_vehicles = ["Ford","Toyota","Mercedes","Wolkswagen","Hyundai","Tesla","BMW"]
list_vehicles[1] = "Ferrari"
list_vehicles.append("Renault") 
list_vehicles.insert(3, "Porsche") # you can use insert method to index adding
list_vehicles.remove("BMW")
list_vehicles.pop(2) # you can also delete with index number with pop method
del list_vehicles[3] # also you can delete everyone of your list with this method, just don't use index and delete
# also if you do use list_vehicle.clear method, your list is cleaned and empty now

print(list_vehicles.sort()) # you can sort with this method to ascending
print(list_vehicles)
print(list_vehicles.count("Hyundai")) # It's showing us to this value count in list
print(list_vehicles.index("Ford")) # you can learn your searched value index with this method

does_exist_vehicle = "Ford" in list_vehicles # if "Ford" or other vehicles doesn't exist, output will be False
print(does_exist_vehicle)

# End of the Day 5

#------------------

# Start of the Day 6

# TUPLES

# 2 type of the create tuple

tuple1 = ()
tuple2 = tuple()

tuple_examp = ("Electro Guitar", "Bass Guitar", "Vocal", "Keyboard", "Drum")
tuple_persons = ("Lemmy", "Peter", "Tony", "Ronnie", "James")

print(len(tuple_examp))
print("I'm using "+ tuple_examp[0] +" to my main entrument") # we can call with index number
print(tuple_examp[-1]) # we can call negative index number, same the lists
print(tuple_examp[0:6]) # we can call values with strings to indexs

tuple_examp = list(tuple_examp)
tuple_examp = tuple(tuple_examp) # we can convert list to tuple or tuple to string

print("Electro Guitar" in tuple_examp) # we can check any item with in method

# tuple_examp[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

united_tuple = tuple_examp + tuple_persons # we can create joined tuples
print(united_tuple)

del united_tuple
del tuple_persons # we can delete with this command becasue methods are not used much in tuples

# End of the Day 6

#-----------------

# Start of the Day 7

# SETS

# 2 type of create set

"""
set1 = {}
set2 = set()

set_examp = {"Motörhead", "Type O Negative","Black Sabbath", "Dio", "Metallica"}
set_exl = {"Iron Maiden", "Judas Priest", "Megadeth, Black Sabbath", "Motörhead"}

print(set_examp)
print(len(set_examp))

print("Does set set_examp contain Dio ? ", "Dio" in set_examp)

set_examp.add("Led Zeppelin") # we can add with this method
# set_examp.update("Iron Maiden") # Each letter or digit of the value added with the update method is used one by one, without repeating the same
set_examp.remove("Metallica") # we can remove anything inside of this set with this method
set_examp.pop() # we can remove 1 value to random with this method
# set_examp.clear() # we can clear this set with method
# del set_examp # we can delete this set to del method
print(set_exl.intersection(set_examp)) # we can use intersection method to show both
print(set_examp.difference(set_exl)) # we can use difference method to find different values both
"""

"""
set_united = set_examp.union(set_exl)
print(set_united)
"""

"""
set01 = {"Light", "Heavy", "Mid-Weight"}
set01 = list(set01)
print(type(set01))
set01 = set(set01)
print(type(set01))
"""

# Checking Subset and Super Set

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

# Finding Symmetric Difference Between Two Sets

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# End of the Day 7

#------------------

# Start of the Day 8

# DICTIONARIES

# 2 type of create dictionary

"""
dict1 = {}
dict2 = dict()

# dictionary struct

person = {
    "name" : "Fırat",
    # Key --- Value
    "surname" : "Çakır",
    "age" : 18,
    "country" : ["Turkey"]
}

print(person['name']) # this is callin a name key to print value (Fırat)
print(len(person)) # this is just showing all key-value couple length

# item adding to dictionaries

person["height"] = 183
person["country"] += ["Albania"]

person["age"] = 19 # we can change any value so easily

# METHODS

print(person)
print("name" in person) # just keys is showing with this method, not for value

person.pop("age") # we can delete with this method to dict items with key names, and deleting with value
person.popitem() # this method is deleting last keys and value
print(person)
del person["country"] # aaand we can any keys and item too
person.clear() # we can clear our dictionary with this method
del person # and yes, we can delete with delete method this dictionary, classicly
"""

"""
band1 = {
    "lead vocal" : "Mustaine",
    "rythm guitar" : "Mustaine",
    "lead guitar" : "Loureiro",
    "bass guitar" : "LoMenzo",
    "drum" : "Verbeuren",
    "back vocal" : ["Loureiro", "LoMenzo"]
}

band1_copy = {
    "any" : "whatever"
}

band1_copy = band1.copy() # we can copy this method, deleting inside of everything in copied place
print(band1_copy.keys()) # we can call every key in inside of dictionary
print(band1_copy.values()) # we can call every value in inside of dictionary
"""

# End of the Day 8

#-------------------

# Start of the Day 9

# IF ELIF ELSE

# if

inputed_number = int(input("Enter a Number: ")) # you can want user input with this input method and input is basicly coming to string, you can change that

"""
if inputed_number > 15: # if you want any output with condition, you can use if, if elif,if else, if elif else methods, just 3 unit
    print("Your number is bigger than 15")
"""

# if else

"""
if inputed_number > 15:
    print("Your number is bigger than 15")
else:
    print("Your number is smaller then 16") # if first is method don't useful, we can use else for anything. Don't need condition
"""

# if elif else

"""
if inputed_number > 15:
    print("Your number is bigger than 15")
elif inputed_number == 0:
    print("Your number is 15") # we can use endless elif and if method but we can use else method just one time
else:
    print("Your number is smaller than 15") # if first is method don't useful, we can use else for anything. Don't need condition
"""

"""
print("Number is bigger than 15") if inputed_number > 15 else inputed_number == 0: print("Number isn't 15") # we can use 1-line if else but it isn't recommend
"""

# nested conditions

"""
if inputed_number < 16:
    if inputed_number == 15:
        print("Your number is 15")
    else:
        print("Your number smaller than 15")
else:
    print("Your number bigger than 15")
"""

# logical operators
"""
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
"""

"""
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
"""

# End of the Day 9

#-------------------

# Start of the Day 10

# LOOPS

# while

"""
number = 1
while number < 5:
    print(number)
    number += 1
else:
    print(f"Biggest number is {number-1}")
"""

"""
number = 0
while number <= 100:
    print(number)
    number += 1
    if number == 99:
        break # we can use continue like this
"""

# for

"""
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number) # basically work method for to "for"
"""

"""
language = 'Python'
for letter in language:
    print(letter)
"""

"""
for i in range(len(language)):
    print(language[i])
"""

"""
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
"""

"""
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
"""

"""
dict = {
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    }

for key in dict:
    if key == 'skills':
        for skill in dict['skills']:
            print(skill) # JavaScript, React, Node, MongoDB, Python
"""

"""for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
"""

"""
for number in range(6):
    pass
"""

# End of the Day 10

#-------------------

# Start of the Day 11

# Functions

# define a function

"""
def func_square(a): # we use just "def" command to define a function
    a = a**2
    print(a)
    
func_square(3) # function already have a print func so we don't need use again
# we can assign parameters same "func_square(a=3, b=5)"
"""

"""
def inputed_func():
    number_one = int(input("Enter number one : "))
    number_two = int(input("Enter number two: "))
    total = number_one + number_two
    return total

print(inputed_func()) #sum with function
    """

"""
def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
"""

"""
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
"""

"""
# Default and Arbitrary Number of Parameters in Functions
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
"""

# End of the Day 11

#--------------------

# Start of the Day 12

# MODULES

#Importing a Module

"""
import examplemodule
print(examplemodule.generate_full_name('Firat', 'Cakir')) # Firat Cakir

# Also we can import functions from other imported modules
"""

"""
from examplemodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g #we can rename modules and functions like this
print(fullname('Firat','Cakir'))
print(total(1, 9))
mass = 100
weight = mass * g(9.81)
print(weight)
print(p)
"""

"""
# OS Module
# Using python os module it is possible to automatically perform many operating system tasks. 
# The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.
# import the module
import os
# Creating a directory
os.mkdir("directory1")
# Changing the current directory
os.chdir("path")
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
"""

"""
# Sys Module
# The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. Function sys.argv returns a list of command line arguments passed to a Python script. 
# The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

#Some useful sys commands

# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version

# Statistics Module
# The statistics module provides functions for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

# Math Module
# Module containing many mathematical operations and constants.

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi
print(pi)

# It is also possible to import multiple functions at once

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

# But if we want to import all the function in math module we can use * .

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

# When we import we can also rename the name of the function.

from math import pi as  PI
print(PI) # 3.141592653589793

# String Module

# A string module is a useful module for many purposes. The example below shows some use of the string module.

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Random Module

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
"""

# End of the Day 12

#---------------------

# Start of the Day 13

# LIST COMPREHENSION - LAMBDA 

"""
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)          # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter numbers: let's filter out positive even numbers from the list below
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
"""

# End of the Day 13

#-------------------

# Start of the Day 14

# HIGHER ORDER FUNCTIONS

"""
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<
# (I don't understand how to sum)
def higher_order_function(f,lst): # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1,2,3,4,5])
print(result) # 15
"""

# like use multi func to one process (for higher order func.)
"""
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    else:
        print("Please use 'square','cube' or 'absolute' commands")

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
"""

"""
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
"""

"""
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

# Let us implement the example above with a decorator
# I think we don't need these functions for upper method, nevermind 

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
"""
"""
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Firat", "Cakir",'Turkey')
"""

# Map Functions

"""
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25] # we can use lambda for write less code
"""

"""
cities = ["istanbul", "ankara", "izmir", "adana", "bursa"]
def bigger(city):
    return city.capitalize()

cities_bigger = map(bigger, cities)
print(list(cities_bigger))

# also we can use both of these methods

cities_bigger1 = map(lambda city: city.capitalize(), cities)
print(list(cities_bigger1))
"""

# Filter Functions

"""
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

#------------------------------------------

numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
"""
"""
names = ["Firat", "Kadir", "Furkan", "Rana", "Merve", "Aktila", "Cemal"]
def name_filter(name):
    if len(name) > 5:
        return True
    return False

long_names = filter(name_filter, names)
print(list(long_names))
"""
"""
# Reduce Functions 

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
"""

# End of the Day 14

#----------------------

# Start of the Day 15

# Python Type Errors

# 1-) SyntaxError
# It is the type of error given when you write missing codes or forget things like parentheses and commas.

# 2-) NameError
# Type of error when naming an unassigned variable or breaking the canonical name patterns used for Python.

# 3-) IndexError
# It is the error type given when wrong index number is processed in groups with more than one index.

# 4-) ModuleNotFoundError
# It is the type of error that is given when we call a module that does not exist or call it with the wrong name (both the same thing actually).

# 5-) AttributeError
# If we call a function that is not inside the modules or is used incorrectly, this type of error is received.

# 6-) KeyError
# It is the type of error given when an incorrect operation is made with the key name used in dictionaries.

# 7-) TypeError
# It is the type of error that Python cannot calculate without bringing operations with integer, float, string, boolean or function types to each other and/or without bringing them to the same class.

# 8-) ImportError
# It is the type of error given when we import a function with the wrong name or not from the modules we call.

# 9-) ValueError
# This is the error we get when we try to assign more than one value to a variable, it is usually the type of error we get by assigning something of different classes to a single variable.

# 10-) ZeroDivisionError
# Is the type of error we get when we try to divide a number by 0.

# End of the Day 15

#-------------------

# Start of the Day 16

# Python datetime

"""
# All functions of datetime module
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
"""


# all examples

"""
from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38
"""

# formatting 

"""
from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0
"""
"""
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)
"""

# strptime 

"""
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
"""
"""
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
"""

#Time Objects to Represent Time

"""
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
"""

#Difference Between Two Points in Time Using

"""
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
"""

# Difference Between Two Points in Time Using timedelata

"""
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
"""

# End of the Day 16

#---------------------

# Start of the Day 17

# Exception Handling

"""
try:
    print(10 + '5')
except:
    print('Something went wrong')
"""

"""
from datetime import datetime

now = datetime.now()
year = now.year

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = year - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except:
    print("You entered something wrong value!")
"""

# Packing and Unpacking Arguments in Python
# We use two operators:
# * for tuples
# ** for dictionaries


#Unpacking Lists

"""
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# When we run the this code, it raises an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list.

#--------------------------------------

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
# It's true version
"""
"""
# We can also use unpacking in the range built-in function that expects a start and an end.

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]
"""

"""
# A list or a tuple can also be unpacked like this:

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
"""
"""
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Fırat', 'country':'Turkey', 'city':'Ankara', 'age':18}
print(unpacking_person_info(**dct)) # Fırat lives in Turkey, Ankara. He is 18 years old.
"""
"""
# Packing Lists

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
"""
"""
# Packing Dict

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Fırat",
      country="Turkey", city="Ankara", age=18))
"""
"""
# Spreading in Python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *list_one, *list_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
"""
"""
# Enumerate
# If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.

for index, item in enumerate([20, 30, 40]):
    print(index, item)
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('The country {i} has been found at index {index}')
"""
"""
# Zip
# Sometimes we would like to combine lists when looping through them. See the example below:

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
"""

# End of the Day 17

#-------------------

# Start of the Day 18

# Regular Expressions

"""
# Methods in re Module

# To find a pattern we use different set of re character sets that allows to search for a match in a string.

# import re # to call 
# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string
"""

"""
# Example to RegEx
# to choose and process anything

import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
"""

"""
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None

# The string does not string with I like to teach, therefore there was no match and the match method returned None.
# False process
"""
"""
# Search

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
"""
"""
# Searching for All Matches Using findall
# findall() returns all the matches as a list

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

# other version is:
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
"""
""" 
# Replacing a Substring

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
"""
"""
# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
"""

# Writing RegEx Patterns
"""
# To declare a string variable we use a single or double quote. To declare RegEx variable r''. The following pattern only identifies apple with lowercase, to make it case insensitive either we should rewrite our pattern or we should add a flag.

import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
[]: A set of characters
[a-c] means, a or b or c
[a-z] means, any letter from a to z
[A-Z] means, any character from A to Z
[0-3] means, 0 or 1 or 2 or 3
[0-9] means any number from 0 to 9
[A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
\: uses to escape special characters
\d means: match where the string contains digits (numbers from 0-9)
\D means: match where the string does not contain digits
. : any character except new line character(\n)
^: starts with
r'^substring' eg r'^love', a sentence that starts with a word love
r'[^abc] means not a, not b, not c.
$: ends with
r'substring$' eg r'love$', sentence that ends with a word love
*: zero or more times
r'[a]*' means a optional or it can occur many times.
+: one or more times
r'[a]+' means at least once (or more)
?: zero or one time
r'[a]?' means zero times or once
{3}: Exactly 3 characters
{3,}: At least 3 characters
{3,8}: 3 to 8 characters
|: Either or
r'apple|banana' means either apple or a banana
(): Capture and group
"""

# re.I is seeing big and small characters like "Banana" and "banana", re.I method find both of them. We can use "r'[Aa]" this method too

# Square Bracket

"""
# Let us use square bracket to include lower and upper case

regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
If we want to look for the banana, we write the pattern as follows:

regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
"""

# Escape character(\) in RegEx

"""
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
"""

# One or more times(+)

"""
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!
"""

# Period(.)

"""
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
"""

# Zero or more times(*)

"""
#Zero or many times. The pattern could may not occur or it can occur many times.

regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
"""

# Zero or one time(?)

"""
# Zero or one time. The pattern may not occur or it may occur once.

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
"""

# Quantifier in RegEx

"""
# We can specify the length of the substring we are looking for in a text, using a curly bracket. Let us imagine, we are interested in a substring with a length of 4 characters:

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
"""

# Cart ^

"""
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
"""

# End of the Day 18 

#--------------------

# Start of the Day 19

# File Handling

"""
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

"""
f = open("./Examplefile/Exmp.txt") # It's not working to me 
print(f)
"""

"""
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
As you can see in the example above, I printed the opened file and it gave some information about it. Opened file has different reading methods: read(), readline, readlines. An opened file has to be closed with close() method.

read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

# output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
"""

"""
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
# output
<class 'str'>
This is an
"""

"""
readline(): read only the first line
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
# output
<class 'str'>
This is an example to show how to open a file and read.
"""

"""
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
# output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
"""

"""
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
"""

# Opening Files for Writing and Updating

"""
# To write to an existing file, we must add a mode as parameter to the open() function:

"a" - append - will append to the end of the file, if the file does not it creates a new file.
"w" - write - will overwrite any existing content, if the file does not exist it creates.
Let us append some text to the file we have been reading:

with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
The method below creates a new file, if the file does not exist:

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
"""


# Deleting Files

"""
We have seen in previous section, how to make and remove a directory using os module. Again now, if we want to remove a file we use os module.

import os
os.remove('./files/example.txt')
If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
"""

# File Types

"""
File with txt Extension
File with txt extension is a very common form of data and we have covered it in the previous section. Let us move to the JSON file

File with json Extension
JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.

Example:

# dictionary
person_dct= {
    "name":"Fırat",
    "country":"Turkey",
    "city":"Ankara",
    "skills":["JavaScript", "C","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Fırat', 'country': 'Turkey', 'city': 'Ankara', 'skills': ['JavaScript', 'C', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Fırat",
    "country":"Turkey",
    "city":"Ankara",
    "skills":["JavaScript", "C","Python"]
}'''
"""

# Changing JSON to Dictionary

"""
To change a JSON to a dictionary, first we import the json module and then we use loads method.

import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
# output
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
"""

# Changing Dictionary to JSON

"""
To change a dictionary to a JSON we use dumps method from the json module.

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
# output
# when you print it, it does not have the quote, but actually it is a string
# JSON does not have type, it is a string type.
<class 'str'>
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
"""

# Saving as JSON File

"""
We can also save our data as a json file. Let us save it as a json file using the following steps. For writing a json file, we use the json.dump() method, it can take dictionary, output file, ensure_ascii and indent.

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
"""

# File with csv Extension

"""
CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.

Example:

"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
Example:

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
# output:
Column names are :name, country, city, skills
        Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines:  2
"""

# File with xlsx Extension

"""
To read excel files we need to install xlrd package. We will cover this after we cover package installing using pip.

import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)
"""

# File with xml Extension

"""
XML is another structured data format which looks like HTML. In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute. Example:XML

<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
For more information on how to read an XML file check the documentation

import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
# output
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
"""

# This file selection options is not worked me

# End of the Day 19

#-------------------

# Start of the Day 20

# PIP

# Numpy
# pip install numpy

"""
import numpy

lst = [1, 2, 3, 4, 5, 6, 7, 8]
np_arr = numpy.array(lst)

print(np_arr)
print(np_arr * 2)
print(np_arr + 4)
"""

# Pandas
# pip install pandas
# we just see how can install frameworks, libraries and pip files

"""
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/f%C4%B1rat-%C3%A7akir-4b5b90251/',
    'https://github.com/FratCR',
    'https://twitter.com/FratCakr0',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
"""

#------------------------------

# Uninstalling Packages

# pip uninstall packagename

#---------------------------

# List of Packages

# pip list

#----------------------------------


# Show Package
# To show information about a package

# pip show packagename
"""
pip show pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
"""

# If we want even more details, just add --verbose

"""
pip show --verbose pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy, pytz, python-dateutil
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
"""

# PIP Freeze

"""
Generate installed Python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed Python packages in a Python project.

pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
The pip freeze gave us the packages used, installed and their version. We use it with requirements.txt file for deployment.
"""

# Reading from URL

# pip install requests

"""
We will see get, status_code, headers, text and json methods in requests module:

get(): to open a network and fetch data from url - it returns a response object
status_code: After we fetched data, we can check the status of the operation (success, error, etc)
headers: To check the header types
text: to extract the text from the fetched response object
json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.
"""

"""
import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page
"""

"""
import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries
"""

# Creating a Package

"""
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b

# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
"""

"""
The folder structure of your package should look like this:

─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
Now let's open the python interactive shell and try the package we have created:

asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Asabeneh', 'Yetayeh')
'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'
>>>
As you can see our package works perfectly. The package folder contains a special file called init.py - it stores the package's content. If we put init.py in the package folder, python start recognizes it as a package. The init.py exposes specified resources from its modules to be imported to other python files. An empty init.py file makes all functions available when a package is imported. The init.py is essential for the folder to be recognized by Python as a package.

Further Information About Packages
Database

SQLAlchemy or SQLObject - Object oriented access to several different database systems
pip install SQLAlchemy
Web Development

Django - High-level web framework.
pip install django
Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
pip install flask
HTML Parser

Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
pip install beautifulsoup4
PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.
XML Processing

ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
GUI

PyQt - Bindings for the cross-platform Qt framework.
TkInter - The traditional Python user interface toolkit.
Data Analysis, Data Science and Machine learning

Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
TensorFlow: is a machine learning library built by Google.
Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
Network:

requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
pip install requests
"""

# End of the Day 20

#-------------------

# Start of the Day 21

# Classes and Objects


# Creating a Class

"""
class Person:
  pass
print(Person)
"""

# Creating an Object
# We can create an object by calling the class.

"""
p = Person()
print(p)
"""

"""
class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Fırat')
print(p.name)
print(p)
"""

"""
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Fırat', 'Çakır', 18, 'Turkey', 'Ankara')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

# Output:

# Fırat
# Çakır
# 18
# Turkey
# Ankara
"""

# Object Methods

"""
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Fırat', 'Çakır', 18, 'Turkey', 'Ankara')
print(p.person_info())

# output
# Fırat Çakır is 18 years old. He lives in Ankara, Turkey
"""

# Object Default Methods

"""
class Person:
      def __init__(self, firstname='Fırat', lastname='Çakır', age=18, country='Turkey', city='Ankara'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

# output:
# Fırat Çakır is 18 years old. He lives in Ankara, Turkey.
# John Doe is 30 years old. He lives in Noman city, Nomanland.
"""

# Method to Modify Class Default Values

"""
class Person:
      def __init__(self, firstname='Fırat', lastname='Çakır', age=18, country='Turkey', city='Ankara'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p1.add_skill('Python')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
p2.add_skill('HTML')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# output:

# Fırat Çakır is 18 years old. He lives in Ankara, Turkey.
# John Doe is 30 years old. He lives in Noman city, Nomanland.
# ['HTML', 'CSS', 'JavaScript', 'Python']
# ['HTML']

# Inheritance

class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# output:

# Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
# ['JavaScript', 'React', 'Python']
# Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
# ['Organizing', 'Marketing', 'Digital Marketing']


# Overriding parent method

class Student(Person):
    def __init__ (self, firstname='Fırat', lastname='Çakır',age=18, country='Turkey', city='Ankara', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# Output: 

Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']"""

# End of the Day 21

#---------------------

# Start of the Day 22

# Python Web Scraping

"""
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

# Output:
# 200
"""

"""
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)
"""

# End of the Day 22

#--------------------

# Start of the 23

# Virtual Environment

# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/23_Day_Virtual_environment/23_virtual_environment.md
# go the link and keep forward step by step


# End of the Day 23

#---------------------------

# Start of the Day 24

# Statistics

# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/24_Day_Statistics/24_statistics.md

# NumPy

"""
# How to import numpy
import numpy as np
# How to check the version of the numpy package
print('numpy:', np.__version__)
# Checking the available methods
print(dir(np))
"""

# CREATING NUMPY ARRAY USING

"""
import numpy as np
"""

"""
# Creating int numpy arrays

# Creating python List

python_list = [1,2,3,4,5]

# Checking data types
print('Type:', type (python_list)) # <class 'list'>
print(python_list) # [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])


# Creating float numpy arrays

# Python list
python_list = [1,2,3,4,5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])


# Creating boolean numpy arrays

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])


# Creating multidimensional array using numpy

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)
    
# Output:

# <class 'numpy.ndarray'>
# [[0 1 2]
# [3 4 5]
# [6 7 8]]


# Converting numpy array to list

# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# Output:

# <class 'list'>
# one dimensional array: [1, 2, 3, 4, 5]
# two dimensional array:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# Creating numpy array from tuple

# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]


# Shape of numpy array

nums = np.array([1, 2, 3, 4, 5, 8])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10, 11]])
print(three_by_four_array.shape)
    
# Output: 

# [1 2 3 4 5 8]
# shape of nums:  (6,)
# [[0 1 2]
# [3 4 5]
# [6 7 8]]
# shape of numpy_two_dimensional_list:  (3, 3)
# (3, 4)


# Data type of numpy array

int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

# Output:

# [-3 -2 -1  0  1  2  3]
# int32
# [-3. -2. -1.  0.  1.  2.  3.]
# float64

# Size of a numpy array

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 9
"""

# Mathematical Operation using numpy

"""
# Mathematical Operation
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)

# Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)

# Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)

# Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)

# Modulus; Finding the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)

# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)

# Exponential is finding some number the power of another:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)
"""

# Checking data types

"""
#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
"""

# Converting types

"""
# Int to Float
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr)

# Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)

# Int ot boolean
print(np.array([-3, -2, 0, 1, 2, 3], dtype='bool'))

# Int to str
# print(numpy_float_list.astype('int').astype('str'))
# array(['1', '2', '3'], dtype='<U21')
# ?
"""

# Multi-dimensional Arrays

"""
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

# Output:

# <class 'numpy.ndarray'>
# [[1 2 3]        
#  [4 5 6]        
#  [7 8 9]]       
# Shape:  (3, 3)  
# Size: 9
# Data type: int32
"""

# Getting items from a numpy array

"""
# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)
"""

# Slicing Numpy array

"""
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)


# How to reverse the rows and the whole array?

print(two_dimension_array[::])

# Output:

# [[1 2 3]
# [4 5 6]
# [7 8 9]]


# Reverse the row and column positions

two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(two_dimension_array[::-1,::-1])

# Output:

# [[9 8 7]
# [6 5 4]
# [3 2 1]]


# How to represent missing values ?

print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

# Output:

# [[1 2 3]
# [4 5 6]
# [7 8 9]]
# [[ 1  2  3]
# [ 4 55 44]
# [ 7  8  9]]


# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C')
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

# Output:

# [[0 0 0]
# [0 0 0]
# [0 0 0]]


# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

# Output:

# [[1 1 1]
# [1 1 1]
# [1 1 1]]


twoes = numpy_ones * 2
print(twoes)

# Output:

# [[2 2 2]
# [2 2 2]
# [2 2 2]]


# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

# Output:

# [[1 2 3]
# [4 5 6]]
# [[1 2]
# [3 4]
# [5 6]]


flattened = reshaped.flatten()
print(flattened)

# Output:

# [1 2 3 4 5 6]


## Horitzontal Stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print(np_list_one + np_list_two)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

# Output:

# [5 7 9]
# Horizontal Append: [1 2 3 4 5 6]



## Vertical Stack
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

# Output:

# Vertical Append: [[1 2 3]
# [4 5 6]]


# Generating Random Numbers

# Generate a random float  number
random_float = np.random.random()
print(random_float)

# Generate a random float  number
random_floats = np.random.random(5)
print(random_floats)

# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 11)
print(random_int)

# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
print(random_int)

# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
print(random_int)


# Generationg random numbers

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
print(normal_array)


# Numpy and Statistics

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
"""

# Matrix in numpy

"""
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)


# Numpy numpy.arange()

# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
print(lst)

for l in lst:
    print(l)
    
# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)

odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

even_numbers = np.arange(2, 20, 2)
print(even_numbers)
"""

"""
# Creating sequence of numbers using linspace

# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
print(np.linspace(1.0, 5.0, num=10))

# not to include the last value in the interval
print(np.linspace(1.0, 5.0, num=5, endpoint=False))

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

print(np.logspace(2, 4.0, num=4))

# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
print(x)
print(x.itemsize)

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
print(np_list)

print('First row: ', np_list[0])
print('Second row: ', np_list[1])

print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])
"""

# NumPy Statistical Functions with Example

"""
Numpy Functions:
Min np.min()
Max np.max()
Mean np.mean()
Median np.median()
Varience
Percentile
Standard deviation np.std()
"""

"""
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))


# How to create repeating sequences?

a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))


# How to generate random numbers?

# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)

rand2 = np.random.randn(2,2)
print(rand2)

# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
print(rand_int)
"""

"""
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax

# numpy.dot(x, y, out=None)


# Linear Algebra

# Dot Product

## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23


# NumPy Matrix Multiplication with np.matmul()

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)

## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)

np.linalg.det(i)

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

new_list = [ x + 2 for x in range(0, 11)]
print(new_list)

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
"""

# End of the Day 24

#-------------------

# Start of the Day 25

# Pandas

# Pandas is an open source, high-performance, easy-to-use data structures and data analysis tools for the Python programming language. 
# Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames. Pandas provides tools for data manipulation:

# reshaping
# merging
# sorting
# slicing
# aggregation
# imputation. If you are using anaconda, you do not have install pandas.


# Importing Pandas

"""
import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np


# Creating Pandas Series with Default Index

nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

# Creating Pandas Series with custom index

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# Creating Pandas Series from a Dictionary

dct = {'name':'Fırat','country':'Turkey','city':'Ankara'}

s = pd.Series(dct)
print(s)

# Creating a Constant Pandas Series

s = pd.Series(10, index = [1, 2, 3])
print(s)

# Creating a Pandas Series Using Linspace

s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)


# DataFrames

# Creating DataFrames from List of Lists

data = [
    ['Fırat', 'Turkey', 'Ankara'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

# Creating DataFrame Using Dictionary

data = {'Name': ['Fırat', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Ankara', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# Creating DataFrames from a List of Dictionaries

data = [
    {'Name': 'Fırat', 'Country': 'Turkey', 'City': 'Ankara'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
"""

"""
# Reading CSV File Using Pandas

import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)


# Data Exploration

print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method

print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method

print(df.shape) # as you can see 10000 rows and three columns

heights = df['Height'] # this is now a series
print(heights)

weights = df['Weight'] # this is now a series
print(weights)

print(len(heights) == len(weights))

print(heights.describe()) # give statisical information about height data

print(weights.describe())

print(df.describe())  # describe can also give statistical information from a dataFrame
"""


# Modifying a DataFrame


# Creating a DataFrame

"""
import pandas as pd
import numpy as np
data = [
    {"Name": "Fırat", "Country":"Turkey","City":"Ankara"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

# Adding a New Column

weights = [84, 78, 69]
df['Weight'] = weights
print(df)

heights = [183, 175, 169]
df['Height'] = heights
print(df)

# Modifying column values

df['Height'] = df['Height'] * 0.01
print(df)

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()
print(bmi)

# Formating DataFrame columns

df['BMI'] = bmi
print(df)

birth_year = ['2004', '1985', '1990']
current_year = pd.Series(2023, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)

# Checking data types of Column values

print(df.Weight.dtype) # int.64

df['Birth Year'].dtype # it gives string object , we should change this to number
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now

# Now same for the current year
df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype

ages = df['Current Year'] - df['Birth Year']
print(ages)

df['Ages'] = ages
print(df)

mean = (35 + 30)/ 2
print('Mean: ',mean)	#it is good to add some description to the output, so we know what is what

print(df[df['Ages'] > 20])

print(df[df['Ages'] < 20])
"""

# End of the Day 25

#-------------------

# Start of the Day 26

# Python for web

# Flask

"""
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
"""

# Go and look flask html sites and app.py

# End of the Day 26

#--------------------

# Start of the Day 27

# Python with MongoDB

# MongoDB

# MongoDB is giving error and i'll continued that

# End of the Day 27

#--------------------

# Start of the Day 28

# Application Programming Interface(API)

# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/28_Day_API/28_API.md

# End of the Day 28

#-------------------

# Start of the Day 29

# Building an API

# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/29_Day_Building_API/29_building_API.md 

# End of the Day 29

#--------------------

# Start of the Day 30

# Congrats, you did it

# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/30_Day_Conclusions/30_conclusions.md

# End of the Day 30
