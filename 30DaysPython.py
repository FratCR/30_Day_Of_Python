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
