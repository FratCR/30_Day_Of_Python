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

